"""
URL configuration for ebazar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from bazar.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('products/', products, name='products'),
    path('productdetails/<int:pk>/', productdetails, name='productdetails'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('update-quantity/<int:product_id>/', update_quantity, name='update_quantity'),
    path('proceed-to-checkout/', proceed_to_checkout, name='proceed_to_checkout'),
    path('checkout/', checkout, name='checkout'),
    path('pay_now/', pay_now, name='pay_now'),
    path('orderconfirm/', orderconfirm, name='orderconfirm'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()