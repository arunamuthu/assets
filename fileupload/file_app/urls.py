from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AssetView, AssetDetailView,TypeView,TypeDetailView,TypeAreaView,TypeAreaDetailView

urlpatterns = [
    path('upload/', AssetView.as_view()),
    path('detail/', AssetView.as_view()),
    path('detail/<int:pk>/', AssetDetailView.as_view()),
    path('type/', TypeView.as_view()),
    path('type/<int:pk>/', TypeDetailView.as_view()),
    path('type-area/', TypeAreaView.as_view()),
    path('type-area/<int:pk>/', TypeAreaDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)