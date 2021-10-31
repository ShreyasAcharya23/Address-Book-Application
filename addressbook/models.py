from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
