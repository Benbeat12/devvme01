from django.conf.urls.static import static
from IT import settings
from django.urls import path
from services.views import service_index, service_detail

app_name = "services"



urlpatterns = [

    path("p_index/", service_index, name="p_index"),
    path("service_detail/", service_detail, name="service_detail"),
    path('service/', service_index, name="services"),
    path("service/<str:slug>/", service_detail, name="service"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)