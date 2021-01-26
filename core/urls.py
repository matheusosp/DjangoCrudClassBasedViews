from django.urls import path

from .views import IndexView, CreateProductView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateProductView.as_view(), name='add_product')

]