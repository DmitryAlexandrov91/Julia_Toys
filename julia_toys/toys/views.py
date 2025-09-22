from django.views.generic import ListView

from toys.models import Toy


class ToyListView(ListView):
    template_name = 'toys/toys.html'
    model = Toy
    context_object_name = 'toys'
