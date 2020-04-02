from django.conf.urls import url
from .views import ImageView

urlpatterns = [
    url(r'^reduce/quality/$', ImageView.as_view(), name='image-reduce-quality'),
]