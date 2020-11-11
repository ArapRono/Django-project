from django.db import models

# Create your models here.
class Houses(models.Model):
    county = models.CharField(max_length = 20 ,blank = False) #Mandatory
    region = models.CharField(max_length = 20, blank = False) #Mandatory
    estate = models.CharField(max_length= 20, blank = False)#Mandatory
    description = models.TextField(blank = False)#Mandatory
    image_1 = models.ImageField(upload_to = "pics" ,blank = False)#Mandatory
    image_2 = models.ImageField(upload_to = "pics" ,blank = False)#Mandatory
    image_3 = models.ImageField(upload_to = "pics" ,blank = False)#Mandatory
    image_4 = models.ImageField(upload_to = "pics", blank = True) #optional
    image_5 = models.ImageField(upload_to = "pics", blank = True) #optional
    desposit = models.IntegerField(blank = True, null = True)  #optional
    rent = models.IntegerField(blank=False, null = True)  # Mandatory
    electricitybills = models.IntegerField(blank=True,null = True)  # optional
    waterbills = models.IntegerField(blank=True,null = True)  # optional
    security_Good = models.BooleanField(default = False,blank = True)  #optional
    security_Very_Good = models.BooleanField(default = False,blank = True) #optional
    security_Excellent = models.BooleanField(default = False,blank=True)  #optional
    singleroom = models.BooleanField(default = False, blank = True)  #optional
    bedsitter = models.BooleanField(default=False, blank = True)  #optional
    bedroom_size = models.IntegerField(blank=True,null = True)  # optional
        
