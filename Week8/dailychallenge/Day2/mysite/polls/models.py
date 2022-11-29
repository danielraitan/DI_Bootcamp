from django.db import models

class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=200)

class Post(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=Person, on_delete=models.CASCADE)

class Persons(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)

