from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'', include('transportation_app.urls')),
    path('admin/', admin.site.urls),
    path('transport/', include('transportation_app.api.urls')),
    path('user/', include('user_app.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]
