"""receipe URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from delicious import views as delicious

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',delicious.base),
    path('',delicious.home,name='home'),
    path('item/<int:pk>',delicious.items,name='food_item'),
    path('menu/',delicious.menu,name='menu'),
    path('menu/<slug:data>',delicious.menu,name='menu_item'),
    path('add-to-cart/',delicious.add_to_cart,name='add-to-cart'),
    path('cart/',delicious.show_cart,name='showcart'),
    path('reg/',delicious.register,name='registration'),
    path('login/',delicious.login, name='login_data'),
    path('logout/',delicious.logout, name='logout_data'),
    path('about/',delicious.about,name='about'),
    path('blog/',delicious.founders,name='blog'),
    path('ad/',delicious.ads,name='advertisement'),
    path('ad/<int:pk>',delicious.ad_details,name='details'),
    path('exec/',delicious.executive,name='executive'),
    path('ex/<int:pk>',delicious.ex_details,name='ex_details'),
    path('removecart/',delicious.remove_cart),
    path('pluscart/',delicious.plus_cart),
    path('minuscart/',delicious.minus_cart),
    path('owl/',delicious.owl),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)