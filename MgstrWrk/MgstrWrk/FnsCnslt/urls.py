"""
Definition of urls for MgstrWrk.
"""

from datetime import datetime
from django.urls import path
from . import views


urlpatterns = [
    path('', views.FinConsul, name='finform'),
    path('finresult/', views.ResultNeiron)
]