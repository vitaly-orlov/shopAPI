from django.views.generic import ListView
from product.models import Product

class Home(ListView):
    template_name = 'pages/home.html'
    queryset = Product.objects.order_by('-id')[:5]
    context_object_name = 'products'
