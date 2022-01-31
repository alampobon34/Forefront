from django.contrib import admin
from foreFrontApp.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username','is_active', 'is_admin']
admin.site.register(User,UserAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'name','subject']
admin.site.register(ContactUs,ContactUsAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'url','image1']
admin.site.register(News,NewsAdmin)


class NewsTellerAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at', 'updated_at']

admin.site.register(NewsTeller, NewsTellerAdmin)
