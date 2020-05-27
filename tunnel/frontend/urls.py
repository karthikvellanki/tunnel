from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.index),
    path('signup', views.index),
    path('account/change-email', views.index),
    path('account/change-password', views.index),
    path('docs', views.index)
]
