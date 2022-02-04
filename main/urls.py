from django.urls import path
from . import views



urlpatterns = [
    path('drugs/', views.drug_list),
    path('batches/', views.drug_batch_list),
    path('alerts/', views.alert_list),
]