from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator,MinValueValidator,MaxValueValidator,MaxLengthValidator

class Department_Model(models.Model):
    name= models.CharField(unique=True,max_length=100)
    location=models.CharField()

    def __str__(self):
        return f'{self.name} --{self.location}'

class Employe_Model(models.Model):
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    desigination=models.CharField(max_length=200)
    Department=models.ForeignKey(Department_Model,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} --{self.salary}--{self.desigination}--{self.Department}'

    def clean(self):
        if self.salary<=5000:
            raise ValidationError  ("The salary must be greater than 5000")
        
class Profile_Model(models.Model):
    employee=models.OneToOneField(Employe_Model,on_delete=models.CASCADE)
    email=models.EmailField()
    phone=models.IntegerField(max_length=10)
    address=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.employee} --{self.email}--{self.phone}--{self.address}'

