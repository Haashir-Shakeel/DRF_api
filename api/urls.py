from django.urls import path,include

from api.views import BookView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book',BookView,basename='bookview')

urlpatterns=[
    path('api/',include(router.urls)),
    path('api/<int:pk>/',include(router.urls)),
]