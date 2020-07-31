from django.contrib import admin
from  testapp.models import Movies
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = [ 'Title','Release_Date','Rating','Director', 'Writer','Actor','Production','Summary'  ,'Language','Country','posters' ,'Trailer']
admin.site.register(Movies,MovieAdmin)