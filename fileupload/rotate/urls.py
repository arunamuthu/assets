from django.conf.urls import url
from .views import ImageView

urlpatterns = [
    url(r'^rotate/$', ImageView.as_view(), name='image-rotate'),
]