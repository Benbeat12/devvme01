
from django.conf.urls.static import static
from IT import settings
from accueil.views import index
from contact.views import contact
from VMEServices.views import service_index, service_detail, product_detail
from django.contrib import admin
from django.urls import path, include
from register import views
from helpdeskApp import views as v

handler404 = v.handler404
app_name = "contact"

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path('register/', views.register, name='register'),
    path("contact/", contact, name="contact"),
    path('helpdeskApp/', include('helpdeskApp.urls')),
    path('contact/', include('contact.urls')),
    path('VMEServices/', include('VMEServices.urls')),
    path('VMEServices/', service_index, name="VMEServices"),
    path("VMEServices/<str:slug>/", service_detail, name="VMEServices"),
    path('product/<str:slug>/', product_detail,  name="product"),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

