from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=69,blank=False)
    Address = models.TextField(max_length=620,blank=False)
    phone =  models.CharField(max_length=12,blank=False)

    def __str__(self):
        return self.name