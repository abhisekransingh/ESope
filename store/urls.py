
from .views import index,signUp,login
from django.urls import path
urlpatterns = [
    path('', index,name="homepage"),
    path('signUp', signUp),
    path('login', login),
]
 