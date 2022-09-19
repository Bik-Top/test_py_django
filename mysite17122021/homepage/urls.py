"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls.conf import path

from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cars/', cars, name='cars'),
    path('car/<slug:carid>/', show_car, name='car'),
]