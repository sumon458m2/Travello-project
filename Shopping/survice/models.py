from django.db import models
class survice(models.Model):
    title=models.CharField(max_length=20,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)
    description = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return self.title

       