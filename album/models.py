from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('author-list')

class Publisher(models.Model):
    name = models.CharField(max_length=60)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publisher-list')

class Book(models.Model):
    title = models.CharField(max_length=100)
    id_author = models.ForeignKey('Author', on_delete=models.PROTECT)
    id_publisher = models.ForeignKey('Publisher', on_delete=models.PROTECT)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-list')
