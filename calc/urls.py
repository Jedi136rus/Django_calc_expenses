from django.contrib import admin
from django.urls import path
from finance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calc, name='home'),
]
