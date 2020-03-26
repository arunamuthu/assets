from django.conf.urls import url
from .views import ImageView

urlpatterns = [
    url(r'^resize/$', ImageView.as_view(), name='image-resize'),
]