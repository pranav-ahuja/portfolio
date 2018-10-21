from django.db import models
class blog(models.Model):
    title=models.CharField(max_length=30)
    datentime=models.DateTimeField(auto_now=False)
    image = models.ImageField(upload_to='images/') 
    body= models.TextField()
# Create your models here.
