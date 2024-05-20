from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, AttractionViewSet, HotelViewSet, CafeViewSet, ClientViewSet, RestaurantViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'attractions', AttractionViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'cafes', CafeViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
