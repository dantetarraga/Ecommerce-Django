"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ecommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('create_category/', views.create_category, name='create_category'),    
    path('categories/', views.CategoryAPIView.as_view(), name='all_categories'),    
    path('category/create', views.CategoryAPIView.as_view(), name='create_category'),   
    path('category/<int:category_id>/update', views.CategoryAPIView.as_view(), name='update_category'),   
    path('category/<int:category_id>/delete', views.CategoryAPIView.as_view(), name='delete_category'), 

    path('size/all', views.SizeAPIView.as_view(), name='all_sizes'),  
    path('size/register/', views.SizeAPIView.as_view(), name='register_size'), 
    path('size/<int:size_id>/update', views.SizeAPIView.as_view(), name='update_size'), 
    path('size/<int:category_id>/delete', views.SizeAPIView.as_view(), name='delete_size'), 

    path('brand/all', views.BrandAPIView.as_view(), name='all_brands'), 
    path('brand/register', views.BrandAPIView.as_view(), name='register_brand'), 
    path('brand/<int:category_id>/update', views.BrandAPIView.as_view(), name='update_brand'), 
    path('brand/<int:category_id>/delete', views.BrandAPIView.as_view(), name='delete_brand'), 

    path('products/', views.ProductAPIView.as_view(), name='all_products'), 
    path('product/register/', views.CategoryAPIView.as_view(), name='register_product'), 
    path('product/<int:category_id>/update', views.ProductAPIView.as_view(), name='update_product'), 
    path('product/<int:category_id>/delete', views.ProductAPIView.as_view(), name='delete_product'), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
