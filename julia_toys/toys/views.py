from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import ListView

from toys.models import Toy


class ToyListView(ListView):
    """Отображение главной страницы с игрушками."""

    template_name = 'toys/toys.html'
    model = Toy
    context_object_name = 'toys'

    def get_queryset(self) -> QuerySet[Any]:
        """Подгрузка к кверисету связанных изображений."""
        queryset = super().get_queryset()
        return queryset.prefetch_related('images')
