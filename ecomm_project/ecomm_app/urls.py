from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name='home'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('about_us',views.about_us,name='about_us'),
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('<int:id>/',views.product_detail,name='product_detail'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('add_to_cart/<int:pid>/',views.add_to_cart,name='add_to_cart'),
    path('buy',views.buy,name='buy'),
    # path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('category/<str:category_name>/', views.category_wise_product, name='category_wise_product'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)