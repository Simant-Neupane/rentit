from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
class Profile(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('tenant', 'Tenant'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class PerportyType(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    perportyType = models.ForeignKey(PerportyType, on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    location = models.CharField(max_length=200,null=True)
    disc = models.TextField(null=True)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.image.name)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(region='NP')
    message = models.TextField()


    

    
