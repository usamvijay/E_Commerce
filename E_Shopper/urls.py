"""E_Shopper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Myapp import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('/', admin.site.urls),

    #site url's Hare.....

    path('index/', views.index),
    path('vijay/<int:id>', views.vijay, name="vijay"),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('login_view/', views.login_view),
    path('logout/', views.logout),
    path('shop/', views.shop),
    path('update_profile/<int:id>', views.update_profile),
    path('change_password/<int:id>', views.change_password),
    path('Register/', views.Register),
    path('user_data/', views.user_data),
    path('profile/', views.profile),
    path('login_data/', views.login_data),
    


    #..../////ADMIN URLS///....

    path('Catagories/', views.Catagories),
    path('admin/', views.Custumers),
    path('Products/', views.Products),
    path('adding_Products/', views.adding_Products),
    path('delete_catagory/<int:id>', views.delete_catagory),
    path('delete_products/<int:id>', views.delete_products),
    path('product_details/<int:id>',views.product_details, name="display"),
    path('add_Catagories/', views.add_Catagories),
    path('edit_catagory/<int:id>', views.edit_catagory),
    path('update_products/<int:id>',views.update_products),
    
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
