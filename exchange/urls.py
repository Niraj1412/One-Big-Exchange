from django.urls import path, include
from rest_framework import routers
from market.views import TopOfTheBookViewSet, OrderViewSet  # Update the import

router = routers.DefaultRouter()
router.register(r'top-of-the-book', TopOfTheBookViewSet)  # Change the view name here
router.register(r'orders', OrderViewSet)  # Change the view name here

urlpatterns = [
    path('api/', include(router.urls)),
]
