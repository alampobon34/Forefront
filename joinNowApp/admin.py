from django.contrib import admin
from joinNowApp.models import *
# Register your models here.

class JoinNowAdmin(admin.ModelAdmin):
    list_display = ['email', 'name','phone']
admin.site.register(joinNow,JoinNowAdmin)