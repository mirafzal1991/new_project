from django.urls import path
from app.views import report

urlpatterns = [
    path('report/', report,name='report'),




]