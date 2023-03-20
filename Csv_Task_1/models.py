from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Country(models.Model):
    country_user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    country_name=models.CharField(max_length=255,null=False,blank=False)
    last_update=models.DateField(auto_now=True)

    def __str__(self):
        return self.country_name
    
class City(models.Model):
    city_country=models.ForeignKey(Country,null=True,blank=True,related_name='country_city',on_delete=models.CASCADE)
    city_name=models.CharField(max_length=255,null=False,blank=False)
    last_update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_name

class Address(models.Model):
    address_user=models.ForeignKey(User,null=True,blank=True,related_name='user_address',on_delete=models.CASCADE)
    address_city=models.ForeignKey(City,null=True,blank=True,related_name='city_address',on_delete=models.CASCADE)
    address=models.CharField(max_length=255,null=False,blank=False)
    pin_code=models.CharField(max_length=8,blank=False,default=323223)

    def __str__(self):
        return self.address
    
class Film(models.Model):
    title=models.CharField(max_length=255,null=False,blank=False)
    description=models.TextField()
    length=models.IntegerField()
    rental_duration=models.DecimalField(max_digits = 5,
                         decimal_places = 2)
    created_date=models.DateTimeField(auto_now=True)
    last_update=models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title 

    