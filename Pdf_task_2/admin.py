from django.contrib import admin
from .models import *
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf 
import datetime
# Register your models here.

class FilmAdmin(admin.ModelAdmin):  
   list_display=['title','description','length','rental_duration','created_date','last_update']
   actions=["Generate_Pdf"]
   def Generate_Pdf(self,request,queryset):
    # import pdb;pdb.set_trace()
    pdf = render_to_pdf('invoice_pdf.html',{'address_data':queryset})
    return HttpResponse(pdf, content_type='application/pdf')
admin.site.register(Film,FilmAdmin)
