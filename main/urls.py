from django.urls import path
from .views import all_teams, new_team, edit_team, delete_team

from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, TeamViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = [
    path('teams/', all_teams, name='all_teams'),
    path('new/', new_team, name='new_team'),
    path('edit/<int:id>/', edit_team, name='edit_team'),
    path('delete/<int:id>/', delete_team, name='delete_team'),
    path('', include(router.urls)),
]




