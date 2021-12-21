

from django.urls.conf import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cars/', cars, name='cars'),
    path('car/<slug:carid>/', show_car, name='car'),
]