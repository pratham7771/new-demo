from django.shortcuts import redirect, render
from .forms import signupForm, userformdata
from .models import signupuser
from django.contrib.auth import logout
from django.core.mail import send_mail
from newproject import settings
import requests
import json
import random

# Create your views here.


def index(request):
    if request.method == 'POST':
        if request.POST.get('signup') == 'signup':
            unm = request.POST['username']
            myfrm = signupForm(request.POST)
            if myfrm.is_valid():
                myfrm.save()
                print("Signup successfully")
                request.session['user'] =unm

                mo = request.POST['num']
                otp=random.randint(1111,9999)


                # 
                #sms send
                 # mention url  
                url = "https://www.fast2sms.com/dev/bulk"


                # create a dictionary
                my_data = {
                    # Your default Sender ID
                    'sender_id': 'FSTSMS',

                    # Put your message here!
                    'message':  f'Hello User, Your account has been login! \nYour OTP is {otp}',

                    'language': 'english',
                    'route': 'p',

                    # You can send sms to multiple numbers
                    # separated by comma.
                    'numbers': mo
                }

                # create a dictionary
                headers = {
                    'authorization': '',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }

                # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                #load json data from source
                returned_msg = json.loads(response.text)

                # print the send message
                print(returned_msg['message'])


                #
                # Send Mail:
                # mail_sub = "Account Creation Confirmation!"
                # mail_msg = "Hello User, \nThis is system genrated mail!\nYour account has been created successfully with us!\nHappy Coding\nThanks & Regards\n+91 8460409520 | prathamsorathiya0071@gmail.com"
                # mail_from = settings.EMAIL_HOST_USER
                # mail_to = request.POST["username"]
                # send_mail(mail_sub, mail_msg, mail_from, [mail_to])

                return redirect('home')
            else:
                print(myfrm.errors)

        #Login---------------
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']

            userinfo=signupuser.objects.get(username=unm)
            #print("name:",userid.firstname)
            print("User id :",userinfo.id)

            user = signupuser.objects.filter(username=unm, password=pas)
            if user:
                print("login successfully")
                request.session['user'] =userinfo.username
                #print("username:",unm)
                request.session['userid']=userinfo.id
                return redirect('home')
            else:
                print("login faild...")
        else:
            print("something went worng")
    return render(request,'index.html')


def home(request):
    user=request.session.get('user')
    # userdata=signupuser.objects.get(username=user)
    # #zip=userdata.zipcode
    # lastn=userdata.lastname
    # print(lastn)
    if request.method=='POST':
        userfrm=userformdata(request.POST,request.FILES)
        if userfrm.is_valid():
            userfrm.save()
            print("Your query has been uploaded")
            return redirect('home')
        else:
            print(userfrm.errors)
    else:
        userfrm=userformdata()
    return render(request,'home.html',{'user':user})


def userlogout(request):
    logout(request)
    return redirect('/')


def updateprofile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    id=signupuser.objects.get(id=userid)

    if request.method=='POST':
        signupfrm=signupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm=signupForm(request.POST,instance=id)
            signupfrm.save()
            print("Your profile updated")
            return redirect('home')
        else:
            print(signupfrm.errors)
    else:
        print("Error........")
    return render(request,'updateprofile.html',{'user': user,'userid':signupuser.objects.get(id=userid)})



def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

