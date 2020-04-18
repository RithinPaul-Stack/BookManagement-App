from django.db import models
from authors.models import Author
from datetime import datetime
from datetime import timedelta
# Create your models here.
class Listing(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    genre = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    is_popular = models.BooleanField(default = False)
    list_date = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.title
    
class Borrow(models.Model):
    book_title = models.CharField(max_length = 200, default= 'Library')
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, default='abs@gmail.com')
    phone = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)
    borrowed_date = models.DateTimeField(default=datetime.now, blank=True)
    return_date = models.DateTimeField(default=datetime.now()+ timedelta(days=10), blank=True)
    def __str__(self):
        return self.book_title
