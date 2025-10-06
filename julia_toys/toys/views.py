from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView

from toys.models import Toy


class ToyListView(ListView):
    template_name = 'toys/toys.html'
    model = Toy
    context_object_name = 'toys'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('images')
        return queryset
