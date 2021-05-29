
from django.contrib import admin
from django.urls import path, include
from loan_api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loan_api.urls')),
]
