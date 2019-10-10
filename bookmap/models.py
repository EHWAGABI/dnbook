from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from main.models import *

# Create your models here.

class BookStore(models.Model):
    bookstore_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, default="storename")
    addr = models.TextField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15, null=True)
    site = models.URLField(null=True)
    img = models.ImageField(upload_to='store/', null=True)
    like_count = models.PositiveIntegerField(default=0)
    email = models.EmailField(null=True)
    openhour = models.TextField(null=True)
    boss = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #보스 프로필 데려와야하지않으까..?
    users = models.ManyToManyField(User,through='Scrap', related_name='%(app_label)s_%(class)s_related')

    def __str__(self):
        return self.name

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s, %s' %(self.user,self.store)

class Review(models.Model):
    store = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    content = models.CharField(max_length=200)
    star = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' %(self.store, self.content[:30])