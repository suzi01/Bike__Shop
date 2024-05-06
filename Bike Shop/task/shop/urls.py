from django.urls import path

from .views import MainPageView, BikeView, SuccessDetailsView

urlpatterns = [
    path('bikes/', MainPageView.as_view(), name="bikes"),
    path('bikes/<int:pk>/', BikeView.as_view(), name='bike_details'),
    path('order/<int:order_no>/', SuccessDetailsView.as_view(), name='success')
]
