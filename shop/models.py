import os.path

from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.db.models import ManyToManyField


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='shop/categories/',blank=True)
    thumbnail = models.ImageField(upload_to='shop/categories/thumbnails/',blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            self.create_thumbnail()

    def create_thumbnail(self):
        img_path = self.image.path
        thumb_path = os.path.join(os.path.dirname(img_path),'thumbnail.jpg', os.path.basename(img_path))
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
        img.save(thumb_path)
        self.thumbnail = f'shop/categories/thumbnails/{os.path.basename(img_path)}'
        super().save(update_fields=['thumbnail'])

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='shop/products/',blank=True)
    thumbnail = models.ImageField(upload_to='shop/products/thumbnails/',blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    about = models.TextField()
    likes = ManyToManyField(User, related_name='likes', blank=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            self.create_thumbnail()

    def create_thumbnail(self):
        img_path = self.image.path
        thumb_path = os.path.join(os.path.dirname(img_path),'thumbnail.jpg', os.path.basename(img_path))
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
        img.save(thumb_path)
        self.thumbnail = f'shop/products/thumbnails/{os.path.basename(img_path)}'
        super().save(update_fields=['thumbnail'])

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/products/',blank=True)
