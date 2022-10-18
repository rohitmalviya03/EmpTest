from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Company(models.Model):
    C_id=models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200 ,default="ABC")

    def __str__(self):
        return self.Name
   
class Employes(models.Model):
    E_id =models.IntegerField(primary_key=True)
    C_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    F_name = models.CharField(max_length=200 ,default="ABC")

    Email=models.CharField(max_length=200 ,default="xyz@gmail.com")
    L_name = models.CharField(max_length=200,default="ABC")
    profile_pic=models.ImageField(upload_to ='uploads/')



    
   
    @staticmethod
    def showCustomers():
        return Employes.objects.all() 
    @staticmethod
    def getData(id):
        return Employes.objects.filter(E_id=id)
    @staticmethod
    def getCustomersByStatus(name):
        return Employes.objects.filter(F_name=name)
