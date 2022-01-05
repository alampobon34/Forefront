from django.db import models

# Create your models here.


class joinNow(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=300, null=False, blank=False)
    CV = models.FileField(upload_to="CV_Files",null=False,blank=False)

    def __str__(self):
        return self.email
