from django.db import models

# Create your models here.

class signupuser(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    zipcode=models.IntegerField()
    num = models.PositiveBigIntegerField()

    def __str__(self):
        return self.firstname

class userform(models.Model):
    title=models.CharField(max_length=120)
    option=models.CharField(max_length=120)
    selectfile=models.FileField(upload_to='Myfiles')
    disc=models.TextField()
    username=models.CharField(max_length=50)
