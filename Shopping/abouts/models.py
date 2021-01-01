from django.db import models

class aboutus(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.CharField(max_length=30,blank=False)
    description = models.CharField(max_length=300,blank=False)
    description1 = models.CharField(max_length=350,blank=False)
    def __str__(self):
        return self.name

class lesson(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.CharField(max_length=30,blank=False)
    name1=models.CharField(max_length=25,blank=False)
    description = models.CharField(max_length=340,blank=False)
    name2=models.CharField(max_length=23,blank=False)
    description1 = models.CharField(max_length=350,blank=False)
    name3=models.CharField(max_length=40,blank=False)
    image=models.ImageField(upload_to='lesson/',blank=False)
    def __str__(self):
        return self.name


class team(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.TextField(max_length=30,blank=False)
    image=models.ImageField(upload_to='lesson/',blank=False)
    
    def __str__(self):
        return self.name

class surfing(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.CharField(max_length=30,blank=False)
    description = models.CharField(max_length=300,blank=False)
    image=models.ImageField(upload_to='surfing/',blank=False)
    def __str__(self):
        return self.name