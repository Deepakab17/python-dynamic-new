from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    contact=models.IntegerField()
    qualification=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images/")
    video=models.FileField(upload_to="videos/")
    audio=models.FileField(upload_to="audio/")
    document=models.FileField(upload_to="documents/")


