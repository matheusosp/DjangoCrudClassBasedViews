from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductModelForm


class IndexView(ListView):
    models = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

