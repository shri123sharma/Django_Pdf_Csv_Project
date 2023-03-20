from django.db import models

# Create your models here.
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
