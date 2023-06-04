from django.db import models
from django.db.models import Avg,Min,Max,Count,Aggregate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import receiver

class Customes(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=15)
    password=models.CharField(max_length=150)
    
    @staticmethod
    def loggedin_email(email):
        try:
            
            
           
            return Customes.objects.get(email=email)
        except:
            return False

    def registor(self):
        self.save()
        print('run first')
    def isexit(self):
        return Customes.objects.filter(email=self.email)


    



