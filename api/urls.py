from django.urls import path
from .views import predict_mental_health_view

urlpatterns = [
    path('predict/', predict_mental_health_view, name = 'predict_mental_health')
]