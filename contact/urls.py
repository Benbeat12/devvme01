from django.contrib import admin
from django.urls import path
from contact.views import contact
from . import views
app_name = "contact"

urlpatterns = [

    path("contact/", contact, name="contact"),

]