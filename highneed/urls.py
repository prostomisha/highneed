"""highneed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from events import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('events/', TemplateView.as_view(template_name='events/index.html'), name='events'),
    path('events/', include('events.urls')),
    #path('events/', views.index, name='events'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profil/', views.index2, name='profil'),
    path('koszyk/', views.koszyk, name='koszyk'),
    path('add_koszyk/<int:pk>/', views.koszyk_add, name='koszyk_add'),
    path('<int:pk>/delete/', views.delete_koszyk, name='delete'),
    path('profil/add_event/', views.create),
    path('profil/add_category/', views.createCategory),
    path('all_events/category/<int:pk>/', views.listofcategories, name='listofcategories'),
    path('all_events/<int:news_id>/', views.detail, name='detail'),
    path('all_events/', views.events, name='events'),
    path('all_events/<int:news_id>/like/', views.likepost, name='like'),
    path('calendar/', views.calendar, name='calendar'),
    path('fanpage/', views.fanpage, name='fanpage'),
    path('style/', TemplateView.as_view(
        template_name='events/style.css',
        content_type='text/css')
    ),

    #path('profil/add_event/', TemplateView.as_view(template_name='add_event.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)