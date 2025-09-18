from django.db import models


class Home(models.Model):
    image = models.ImageField(upload_to='images/home')
    type = models.CharField(max_length=120)
    price = models.IntegerField()
    sity = models.TextField(null=True, blank=True)
    location = models.TextField()
    beds = models.TextField(null=True, blank=True)
    baths = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sity


class Customer(models.Model):
    image = models.ImageField(upload_to='images/customer')
    reyting = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=120)
    descriptions = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=120)

    def __str__(self):
        return self.first_name


class Agent(models.Model):
    image = models.ImageField(upload_to='images/agent')
    first_name = models.CharField(max_length=120)
    job = models.CharField(max_length=120)
    descriptions = models.TextField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.first_name
