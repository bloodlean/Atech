from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
=======
from views import add_to_cart, view_cart, remove_from_cart
>>>>>>> 8c4a84435e3f40093a14907c826f0bd9ae76b4d4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search_view, name='search_view'),
    path('advanced_search/', views.advanced_search_view, name='advanced_search'),
    path('category/<int:category_id>/', views.category_view, name='category_view'),
<<<<<<< HEAD
    path('cart/', views.view_cart, name='view_cart'),  
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Исправлено: views.remove_from_cart
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 8c4a84435e3f40093a14907c826f0bd9ae76b4d4
