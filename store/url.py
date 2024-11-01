from django.urls import path
from . import views

# from  django.urls import path
# from . import views


# urlpatterns = [
#    path("index", views.index),
#    path("home", views.homepage)
# ]

urlpatterns = [
    path("products", views.product_list),
    path('products/int:<pk>', views.product_detail)
]