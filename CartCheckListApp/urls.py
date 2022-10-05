from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartCheckListAPIView.as_view(), name="cartchecklists"),
    path('<int:id>', views.CartCheckListDetailAPIView.as_view(), name="cartchecklists"),
]
