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
class Employee1(models.Model):
    name = models.CharField(max_length=100)
    department=models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    profile = models.ImageField(upload_to='employee_profiles/', blank=True, null=True)
    password = models.CharField(max_length=100)
    d_code = models.CharField(max_length=20,null=True)
    d_des = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.name
class Department(models.Model):
    name=models.CharField(max_length=20,null=True)
    code=models.CharField(max_length=50, unique=True,default="N/A")
    description= models.TextField(blank=True)
    def _str_(self):
        return f"{self.name} ({self.code})"
class Query(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    name=models.CharField(max_length=20)
    email=models.EmailField()
    query=models.CharField(max_length=100,blank=False)
    subject=models.CharField(max_length=20,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    solution=models.CharField(max_length=200,null=True)
    def __str__(self):
        return f"{self.name} - {self.query[:30]}..."



