from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import Cart, User, DeliveryCost
from apps.products.models import Product

from .serializers import UserSerializer, CartSerializer, DeliveryCostSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all().order_by('id')
#     serializer_class = CartSerializer

#     @action(methods=['get'], detail=False, url_path='checkout/(?P<userId>[^/.]+)', url_name='checkout')
#     def checkout(self, request, *args, **kwargs):
#         try:
#             user = User.objects.get(pk=int(kwargs.get('userId')))
#         except Exception as e:
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data={'Error': str(e)})


class CartAPIView(APIView):
    def get(self, request, format=None):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        cart = Cart.objects.get(id=id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeliveryCostViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCost.objects.all().order_by('id')
    serializer_class = DeliveryCostSerializer
