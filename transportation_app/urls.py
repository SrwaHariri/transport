from rest_framework.routers import DefaultRouter

from user_app.api.urls import urlpatterns as user_urlpatterns
from transportation_app.api.urls import urlpatterns as transport_urlpatterns

router = DefaultRouter()

urlpatterns = []

urlpatterns += user_urlpatterns
urlpatterns += transport_urlpatterns

