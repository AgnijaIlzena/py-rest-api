from django.urls import path
from .views import get_investments, create_investment, investment_detail

urlpatterns = [
    path('investments/', get_investments, name='get_investments'),
    path('investments/create', create_investment, name='create_investment'),
    path('investment/<int:pk>', investment_detail, name='investment_detail')
    ]

