from django.contrib import admin
from django.urls import path
#from downloadapp import views, views2
from django.urls import path, include
from . import views
from helloworld import views2
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cv', views.show),
    path('download_pdf', views2.download_pdf),
    path('user_question', views.get_data),
    path('', views.show_login),
    # path('downloadpdf/', views2.download_pdf_file, name='download_pdf_file'),
    # path('downloadpdf//', views2.download_pdf_file, name='download_pdf_file'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)