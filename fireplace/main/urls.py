from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('types_work/', views.types_work, name='types_work'),
    path('thank-you/', views.thank_you, name='thank_you'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)