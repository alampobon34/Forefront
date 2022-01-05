from django.contrib import admin
from foreFrontApp.models import *
# Register your models here.

admin.site.register(User)

admin.site.register(ContactUs)

admin.site.register(News)


class NewsTellerAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at', 'updated_at']


admin.site.register(NewsTeller, NewsTellerAdmin)
