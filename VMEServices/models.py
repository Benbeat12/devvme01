from django.db import models
from django.urls import reverse
import os
from django.template.defaultfilters import slugify


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128, default="")
    description = models.TextField()
    technology = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="services", blank=True, null=True)
    image = models.ImageField(upload_to="services")

    def __str__(self):
        return f"{self.title} ({self.thumbnail})"

    def get_absolute_url(self):
        return reverse("service", kwargs={"slug": self.slug})


class serviceADM(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)



    def __str__(self):
        return f"{self.title} ({self.technology})"

class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.slug), instance)
        return None

    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)


class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.series.slug), slugify(self.article_slug),
                                instance)
        return None

    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)



class Product(models.Model):
    name = models.CharField(max_length=128)
    stripe_product_id = models.CharField(max_length=100, default=0)
    slug = models.SlugField(max_length=128)
    product_price = models.FloatField(default=0.0)
    stok = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stok})"

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})