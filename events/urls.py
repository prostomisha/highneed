from django.urls import path
from django.views.generic import TemplateView

from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_event/', views.create),
    path('add_category/', views.createCategory),
    path('search/', views.search, name='search'),
    path('search_by_date/', views.search_by_date, name='search_by_date'),
    path('all_events/category/<int:pk>/', views.listofcategories, name='listofcategories'),
    path('all_events/<int:news_id>/', views.detail, name='detail'),
    path('all_events/', views.events, name='events'),
    path('all_events/<int:news_id>/like/', views.likepost, name='like'),
    path('style/', TemplateView.as_view(
        template_name='events/style.css',
        content_type='text/css')
    ),
    #path('events/', TemplateView.as_view(template_name='events/main_page.html'), name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)