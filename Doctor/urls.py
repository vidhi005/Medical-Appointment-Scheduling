from django.urls import path
from Doctor.views import *


urlpatterns = [
    path('access/data/', AccessView.get_data),
    path('access/checkin/<str:id>/', AccessView.check_in),
    path('access/checkout/<str:id>/', AccessView.check_out),
]