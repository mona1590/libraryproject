from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)
    
class Address(models.Model):
    city = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)
    def __str__(self):
        return self.name

class Booklab9(models.Model):
    title = models.CharField(max_length= 100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default = 1)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)
        
    def __str__(self):
        return self.name
    
    
    
class BookImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/')
    
    def __str__(self):
        return self.title
    
    