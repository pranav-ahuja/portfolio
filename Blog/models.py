from django.db import models
class blog(models.Model):
    title=models.CharField(max_length=250)
    datentime=models.DateTimeField(auto_now=False)
    image = models.ImageField(upload_to='images/') 
    body= models.TextField()
    def summary(self):
        return self.body[:50]
    def pub_date_pretty(self):
        return self.datentime.strftime('%b %e %Y')
    def __str__(self):
        return self.title
# Create your models here.
