from django.urls import path
from . import views

urlpatterns = [
    path('',views.MapView, name='map'),
    path('temperature/<coord>',views.TempView,name="temp")
]