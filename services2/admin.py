from django.contrib import admin
from services.models import Service, serviceADM, ArticleSeries, Article, Product

class ServicesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServicesAdmin)
admin.site.register(serviceADM)
admin.site.register(ArticleSeries)
admin.site.register(Article)


admin.site.register(Product)




