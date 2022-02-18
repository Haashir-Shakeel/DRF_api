from django.urls import path,include

from api.views import BookView, UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book',BookView,basename='bookview')
router.register('users',UserView)

urlpatterns=[
    path('api/',include(router.urls)),
]