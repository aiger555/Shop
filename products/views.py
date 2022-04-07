from django.http import Http404, HttpResponse
from django.db.models import Q
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import (
    FavoriteSerializer,
    CollectionSerializer,
    ProductSerializer,
    CategorySerializer, 
    ProductImageSerializer,
    ProductColorSerializer,
    AboutUsSerializer,
    AboutUsImageSerializer,
    NewsSerializer,
    AdvantagesSerializer,
    SlaiderSerializer,
    PublicOfferSerializer,
    HelpSerializer,
    FooterSerializer,
    )

from .models import (
                    AboutUs,
                    Advantages,
                    Collection, 
                    Category, 
                    Favorite, 
                    Product, 
                    ProductImage, 
                    ProductColor,
                    AboutUsImage,
                    News,
                    PublicOffers,
                    Slaider,
                    Help,
                    Footer,
                    )


class Pagination(PageNumberPagination):
    page_size = 2
    max_page_size = 3


class SlaiderListAPIView(APIView):
    def get(self, request, format=None):
        slaiders = Slaider.objects.all()
        serializer = SlaiderSerializer(slaiders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SlaiderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionModelViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = Pagination


class ProductListModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = Pagination


class ProductDetailAPIView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category_slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
    
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, category_slug, product_slug):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_slug, product_slug):
        product = self.get_object(category_slug, product_slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryDetailAPIView(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.filter.get(slug=category_slug)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_slug):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_slug):
        category = self.get_object(category_slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductImageListAPIView(APIView):
    def get(self, request, format=None):
        image = ProductImage.objects.all()
        serializer = ProductImageSerializer(image)
        return Response(serializer.data)


class ProductColorListAPIView(APIView):
    def get(self, request, format=None):
        color = ProductColor.objects.all()
        serializer = ProductColorSerializer(color)
        return Response(serializer.data)


class FavoriteListAPIView(APIView):
    def get(self, request, format=None):
        likes = Favorite.objects.all()
        serializer = FavoriteSerializer(likes, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'products': []})


@api_view(['GET'])
def similar_products(request, slug):
    category = Category.objects.get(slug=slug)
    queryset = Product.objects.all().filter(category=category)[0:5]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


class AboutUsListAPIView(APIView):
    def get(self, request, format=None):
        aboutus = AboutUs.objects.all()
        serializer = AboutUsSerializer(aboutus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutUsImageListAPIView(APIView):
    def get(self, request, format=None):
        aboutusi = AboutUsImage.objects.all()
        serializer = AboutUsImageSerializer(aboutusi, many=True)
        return Response(serializer.data)


class NewsModelViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = Pagination


class AdvantagesAPI(APIView):
    def get(self, request, format=None):
        advantages = Advantages.objects.all()
        serializer = AdvantagesSerializer(advantages, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AdvantagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicOfferAPIView(APIView):
    def get(self, request, format=None):
        products = PublicOffers.objects.all()
        serializer = PublicOfferSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PublicOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelpAPIView(APIView):
    def get(self, request, format=None):
        products = Help.objects.all()
        serializer = HelpSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HelpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FooterAPIView(APIView):
    # def get_object(self):
    #     try:
    #         return Footer.objects.get(id)
    #     except Footer.DoesNotExist:
    #         return Http404

    def get(self, request, format=None):
        footer = Footer.objects.all()
        serializer = FooterSerializer(footer, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        footer = Footer.objects.all()
        serializer = FooterSerializer(footer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        footer = Footer.objects.get(id=id)
        footer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
