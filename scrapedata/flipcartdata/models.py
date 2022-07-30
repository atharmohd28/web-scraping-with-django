from django.db import models

# Create your models here.

class Product(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(max_length=100,null=True,blank=True)
    Price=models.CharField(max_length=100,null=True,blank=True)
    Details=models.TextField()

    def __str__(self) :
        return self.Name
