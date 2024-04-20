from django.contrib import admin
from django.urls import path, include
from app import views



urlpatterns = [
    path('',views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/',include('app.urls'))
]