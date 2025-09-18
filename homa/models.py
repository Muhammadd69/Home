from django.db import models



class Home(models.Model):
    image = models.ImageField(upload_to='images/home')
    price = models.IntegerField()
    sity = models.TextField(null=True, blank=True)
    location = models.TextField()


    def __str__(self):
        return self.sity
