
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='payments-home'),
    # only for the Coinbase charges approach
    path('success/', views.success_view, name='payments-success'),
    # only for the Coinbase charges approach
    path('cancel/', views.cancel_view, name='payments-cancel'),
    path('webhook/', views.coinbase_webhook),  # new
]
