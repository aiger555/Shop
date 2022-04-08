from django.urls import path

from .views import (
    BackCallAPIView,
    CollectionModelViewSet,
    CollectionModelViewSet,
    FloatingAPIView,
    HelpAPIView,
    NewsModelViewSet,
    ProductColorListAPIView,
    ProductListModelViewSet, 
    ProductDetailAPIView,
    CategoryDetailAPIView,
    ProductListModelViewSet,
    PublicOfferAPIView,
    search,
    ProductImageListAPIView,
    FavoriteListAPIView,
    AboutUsImageListAPIView,
    AboutUsListAPIView,
    NewsModelViewSet,
    AdvantagesAPI,
    PublicOfferSerializer,
    similar_products,
    FooterAPIView,
)


urlpatterns = [
    path('products/', ProductListModelViewSet.as_view({'get': 'list'})),
    path('products/images/', ProductImageListAPIView.as_view()),
    path('products/colors/', ProductColorListAPIView.as_view()),
    path('products/likes/', FavoriteListAPIView.as_view()),
    path('products/search/', search),
    path('products/similar/', similar_products),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetailAPIView.as_view()),
    path('products/<slug:category_slug>/', CategoryDetailAPIView.as_view()),
    path('aboutus/', AboutUsListAPIView.as_view()),
    path('aboutusi/', AboutUsImageListAPIView.as_view()),
    path('news/', NewsModelViewSet.as_view({'get': 'list'})),
    path('advantages/', AdvantagesAPI.as_view()),
    path('publicoffers/', PublicOfferAPIView.as_view()),
    path('collections/', CollectionModelViewSet.as_view({'get': 'list'})),
    path('help/', HelpAPIView.as_view()),
    path('footer/', FooterAPIView.as_view()),
    path('backcall/', BackCallAPIView.as_view()),
    path('floating/', FloatingAPIView.as_view()),

]