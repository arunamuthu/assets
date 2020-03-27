from django.conf.urls import url
from .views import ImageView

urlpatterns = [
    url(r'^crop/$', ImageView.as_view(), name='image-crop'),
]