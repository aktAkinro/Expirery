from django.urls import path
from . import views



urlpatterns = [
    path('drugs/', views.drug_list),
    path('drugs/<int:id>/', views.drug_detail),
    path('batches/', views.drug_batch_list),
    path('batches/<int:id>/', views.drug_batch_detail),
    path('alerts/', views.alert_list),
    path('alerts/<int:id>/', views.alert_detail),
]