from django.conf.urls import url
from .views import AssetView

urlpatterns = [
    url(r'^upload/$', AssetView.as_view(), name='file-upload'),
]