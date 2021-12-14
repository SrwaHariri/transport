from django.contrib import admin
from transportation_app.models import TransportItem, Color, MainCategory, SubCategory

admin.site.register(TransportItem)
admin.site.register(Color)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
