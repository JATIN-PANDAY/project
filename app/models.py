from django.db import models
from base.models import BaseModel

# Create your models here.

    
class Regestration(BaseModel):
    name = models.CharField(max_length=50, null=True)
    password=models.CharField(max_length=10,null=True)
    image = models.ImageField(upload_to='student/images/', blank=True, null=True)
