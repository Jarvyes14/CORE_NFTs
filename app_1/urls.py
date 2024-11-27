from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.nft_catalog, name='catalogo'),
    path('mint_nft/', views.mint_nft, name='mint_nft'),
]
