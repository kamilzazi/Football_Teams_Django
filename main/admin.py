from django.contrib import admin
from .models import Team, Player, Sponsor

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    # fields = ('name', 'country', 'year', 'description')
    list_display = ('name', 'country', 'year', 'description')
    list_filter = ('year', 'country')
    search_fields = ('name', 'description')

admin.site.register(Player)
admin.site.register(Sponsor)