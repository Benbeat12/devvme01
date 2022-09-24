from django.conf.urls.static import static
from IT import settings
from django.urls import path
from VMEServices.views import service_index, service_detail

app_name = "services"



urlpatterns = [

    path("VMEServices_index/", service_index, name="VMEServices_index"),
    path("service_detail/", service_detail, name="service_detail"),
    path('VMEServices/', service_index, name="services"),
    path("VMEServices/<str:slug>/", service_detail, name="VMEServices"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)