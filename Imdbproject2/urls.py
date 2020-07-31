"""Imdbproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from testapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',views.MoviesListView.as_view() ),
    re_path(r'^(?P<pk>\d+)/$', views.MoviesDetailView.as_view()),
    path('adm/',views.movieslist, name='list_page_show'),
    path('create/',views.MoviesCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<pk>\d+)/$',views.MoviesUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.MoviesDeleteView.as_view()),
    path('search_title/',views.search_title_view),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
