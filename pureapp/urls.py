
from . import views
from django.urls import path
urlpatterns = [
    path('',views.home,name='home'),
    path('homes',views.homes,name='homes'),
    path('homess/<id>',views.homess,name='homess'),
    path('homesss/<id>',views.homesss,name='homesss'),
    path('homessss/<id>',views.homessss,name='homessss'),
    
]
