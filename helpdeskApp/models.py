from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import calendar


# Create your models here.
class NewDevices(models.Model):
    device_name = models.CharField(max_length=30, help_text='Specify device i.e mouse')
    device_serial_num = models.CharField(max_length=30, help_text='Add device serial number')
    device_model = models.CharField(max_length=30, help_text='Add model i.e HP')
    origin = models.ForeignKey(User, on_delete=models.CASCADE)
    device_status = models.CharField(max_length=30, help_text='Add deveice status i.e new or refurbished')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Add All New Devices"

    def __str__(self): 
        return self.device_name

SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

class ReportedDevices(models.Model):
    device_type = models.CharField(max_length=30, choices=SEMESTER_CHOICES,)
    device_serial = models.CharField(max_length=30)
    # device_origin = models.CharField(max_length=30)
    device_origin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    device_issue_description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')

    class Meta:
        verbose_name = "View all Reported Issues"

    def __str__(self):
        return self.device_type





# Create your models here.
"""
product
- Nom
- Prix
- La quantité en stock
- Description
- Image
"""

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stok = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    isPlaying = False

    def __str__(self):
        return f"{self.name} ({self.stok})"

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
