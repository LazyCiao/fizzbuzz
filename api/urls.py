from django.urls import path
from .views import FizzBuzzView, FizzBuzzStatisticsView

urlpatterns = [
    path('fizzbuzz/', FizzBuzzView.as_view(), name='fizzbuzz'),
    path('fizzbuzz/stats/', FizzBuzzStatisticsView.as_view(), name='fizzbuzz_stats'),
]
