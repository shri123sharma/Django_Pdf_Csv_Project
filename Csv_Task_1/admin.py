from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
import tempfile
import zipfile

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    actions = ['DownloadSelectedCsvFile']
    list_display=['country_user','country_name','last_update']

    def DownloadSelectedCsvFile(self,request, queryset,*args):
      f=open('some.csv','w')
      writer = csv.writer(f)
      writer.writerow(['country_user','country_name','last_update'])
      for coun_data in queryset:
        writer.writerow([coun_data.country_user,coun_data.country_name,coun_data.last_update])
      f.close()
      f=open('some.csv','r')
      response = HttpResponse(f, content_type='text/csv')
      response['Content-Disposition'] = 'attachment; filename=country_data.csv'
      return response
admin.site.register(Country,CountryAdmin)

class CityAdmin(admin.ModelAdmin):
    actions=['DownloadSelectedCsvFile']
    list_display=['city_country','city_name','last_update']

    def DownloadSelectedCsvFile(self,request,queryset):
      f=open('city_data.csv','w')
      writer=csv.writer(f)
      writer.writerow(['city_country','city_name','last_update'])
      for city_data in queryset:
         writer.writerow([city_data.city_country,city_data.city_name,city_data.last_update])
      f.close()
      f=open('city_data.csv','r')
      response=HttpResponse(f,content_type='application/msword')
      response['Content-Disposition'] = 'attachment; filename=city_data.csv'
      return response
admin.site.register(City,CityAdmin)

class AdressAdmin(admin.ModelAdmin):
    actions=['DownloadSelectedCsvFile']
    list_display=['address_user','address_city','address','pin_code']
    def DownloadSelectedCsvFile(self,request,queryset):
       f=open('address_data.csv','w')
       writer=csv.writer(f)
       writer.writerow(['user_address','city_address','address','pin_code'])
       for address_data in queryset:
        writer.writerow([address_data.address_user,address_data.address_city,address_data.address,address_data.pin_code])
        f.close()
        f=open('address_data.csv','r')
        response=HttpResponse(f,content_type='text/csv')
        response['Content-Disposition']='attachment;filename=address_data.csv'
        return response
admin.site.register(Address,AdressAdmin)

class FilmAdmin(admin.ModelAdmin):
   
   list_display=['title','description','length','rental_duration','created_date','last_update']
   actions=["Generate_Pdf"]

   def Generate_Pdf(self,request,queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    for add_data in queryset:  
      p.drawString(100, 100,''.join(str([add_data.title,add_data.length,add_data.rental_duration,add_data.last_update,add_data.created_date])))
      p.showPage()
      p.save()
      pdf = buffer.getvalue()
      buffer.close()
      response.write(pdf)
      return response
admin.site.register(Film,FilmAdmin)