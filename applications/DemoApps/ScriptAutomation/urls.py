from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.angular),
    path('', include(('django.contrib.auth.urls', 'django.contrib.auth'), namespace='auth')),
    path('', include(('social_django.urls', 'social_django'), namespace='social')),
]