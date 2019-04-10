from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to = 'images/',blank = True)
    title = models.CharField(max_length = 50)
    company = models.CharField(max_length = 50)
    summary = models.TextField()
    duration = models.CharField(max_length = 50)

class Resume(models.Model):
    desc = models.CharField(max_length = 255, blank = True)
    doc = models.FileField(upload_to = 'static/')

class Skills(models.Model):
    skill = models.CharField(max_length = 255, blank = True)
    image = models.ImageField(upload_to = 'images/',blank = True)
    level = models.IntegerField()

class About(models.Model):
    title = models.CharField(max_length = 100)
    content =  models.TextField()
    focus = models.CharField(max_length = 150)

class Project(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/',blank = True)

class Education(models.Model):
    image = models.ImageField(upload_to = 'images/',blank = True)
    uni_name= models.CharField(max_length = 100)
    add = models.CharField(max_length = 100)
    study = models.CharField(max_length = 100)
    project = models.TextField()

class Contact(models.Model):
    Email = models.EmailField()
    phno = models.IntegerField()
    address = models.TextField(max_length = 500)
    map = models.ImageField(upload_to = 'images/',blank = True)
    facebook = models.URLField(max_length = 200, blank = True)
    twitter = models.URLField(max_length = 200, blank = True)
    linkedin = models.URLField(max_length = 200, blank = True)
    stackover = models.URLField(max_length = 200, blank = True)
