from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)
    
    def __str__(self):
        return self.first_name  

