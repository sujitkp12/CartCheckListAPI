from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CartCheckListSerializer
from .models import CartCheckList
from rest_framework import permissions



class CartCheckListAPIView(ListCreateAPIView):
    serializer_class = CartCheckListSerializer
    queryset = CartCheckList.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class CartCheckListDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartCheckListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CartCheckList.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
