from django.db import models
class destinate(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.TextField(max_length=30,blank=False)
    def __str__(self):
        return self.name
class destination(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.TextField(max_length=30,blank=False)
    description=models.TextField(max_length=500,blank=False)
    image=models.ImageField(upload_to="destinate/",blank=False)
    def __str__(self):
        return self.name


class destin(models.Model):
    name=models.CharField(max_length=20,blank=False)
    description=models.CharField(max_length=300,blank=False)
    def __str__(self):
        return self.name


class destin1(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.TextField(max_length=30,blank=False)
    description=models.TextField(max_length=500,blank=False)
    image=models.ImageField(upload_to="destinate/",blank=False)
    image1=models.ImageField(upload_to="destinate/",blank=False)

    def __str__(self):
        return self.name

class destin2(models.Model):
    date=models.CharField(max_length=20,blank=False)
    title=models.TextField(max_length=30,blank=False)
    description=models.CharField(max_length=500,blank=False)
    image=models.ImageField(upload_to="destination/",blank=False)
    def __str__(self):
        return self.title

class destin3(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.TextField(max_length=30,blank=False)
    description=models.TextField(max_length=500,blank=False)
    image=models.ImageField(upload_to="destin3/",blank=False)
    image1=models.ImageField(upload_to="destin3/",blank=False)

    def __str__(self):
        return self.name
class destin4(models.Model):
    name=models.CharField(max_length=20,blank=False)
    description=models.CharField(max_length=500,blank=False)
    def __str__(self):
        return self.name

class destin5(models.Model):
    name=models.CharField(max_length=20,blank=False)
    title=models.TextField(max_length=30,blank=False)
    description=models.TextField(max_length=500,blank=False)
    image=models.ImageField(upload_to="destin5/",blank=False)
    def __str__(self):
        return self.name
