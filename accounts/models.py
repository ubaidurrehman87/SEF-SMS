from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School_Detail(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50)
    school_code = models.CharField(max_length=50)
    school_category = models.CharField(max_length=50)
    school_address = models.CharField(max_length=150)
    image =models.ImageField( upload_to='pics/', height_field=None, width_field=None, max_length=None)
    
    
