from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=25,null=True)
    #if you recreate a new table you'll need to set its value as null=True because it will allow for  the previous
    #  values of the exact column to be as null, which is in this case True..

    contact=models.IntegerField()
    qualification=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images/")
    video=models.FileField(upload_to="videos/")
    audio=models.FileField(upload_to="audio/")
    document=models.FileField(upload_to="documents/")
    def __str__(self):
        return str(self.name)


