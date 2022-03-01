from django.urls import path
from .views import *
from .models import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('watches', WatchHome.as_view(), name='watches'),
    path('post/<slug:slug>/', WatchesShow.as_view(), name='show'),
    path('contact', contact, name='contact'),
    path('category/<slug:cat_slug>/', WatchCategory.as_view(), name='category')
]