from django.urls import path
from . import views
urlpatterns=[

    path('auth-check',views.auth_check)
]