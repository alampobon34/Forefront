from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from foreFrontApp.models import *
# Create your views here.
import json
import csv


def logout_user(request):
    logout(request)
    #messages.success(request,'Logout Successfully....!!')
    return redirect('admin:login')


def export(request,id):
    try:
        name = id.split("_")
        print(name[1])
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        if name[1]=="newsteller":    
            writer.writerow(['id','email','created_at','updated_at'])
            for row in NewsTeller.objects.all().values_list('id','email','created_at','updated_at'):
                writer.writerow(row)
            response['Content-Disposition'] = 'attachment; filename="Newsteller.csv"'
            return response
        elif name[1]=="contactus":    
            writer.writerow(['id','name','email','subject','message'])
            for row in ContactUs.objects.all().values_list('id','name','email','subject','message'):
                writer.writerow(row)
            response['Content-Disposition'] = 'attachment; filename="ContactUs.csv"'
            return response
        elif name[1]=="news":    
            writer.writerow(['id','title','url','created_at','updated_at'])
            for row in News.objects.all().values_list('id','title','url','created_at','updated_at'):
                writer.writerow(row)
            response['Content-Disposition'] = 'attachment; filename="News.csv"'
            return response
        elif name[1]=="user":
            #writer.writerow(['id','email','username'])
            #for row in User.objects.all().values_list('id','email','username'):
                #writer.writerow(row)
            #response['Content-Disposition'] = 'attachment; filename="Users.csv"'
            #return response
            html="Couldn't download"
            return HttpResponse(html)
        else:
            return render("http://54.198.203.80/admin/foreFrontApp/name[1]/")
    except:
        pass
