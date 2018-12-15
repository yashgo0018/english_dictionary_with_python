from django.contrib import admin
from django.urls import path
from .views import HomeView, ListDataKeys

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/data_keys/', ListDataKeys.as_view(), name='api'),
]
