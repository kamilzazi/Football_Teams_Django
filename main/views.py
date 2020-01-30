from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Team
from .forms import TeamForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# Create your views here.
def all_teams(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})

@login_required
def new_team(request):
    form = TeamForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(all_teams)
    return render(request, 'team_form.html', {'form': form})

@login_required
def edit_team(request, id):
    team = get_object_or_404(Team, pk=id)
    form = TeamForm(request.POST or None, request.FILES or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect(all_teams)
    return render(request, 'team_form.html', {'form': form})

@login_required
def delete_team(request, id):
    team = get_object_or_404(Team, pk=id)
    if request.method == "POST":
        team.delete()
        return redirect(all_teams)
    return render(request, 'confirm.html', {'team': team})


