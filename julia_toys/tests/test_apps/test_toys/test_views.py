from typing import Any, Callable

import pytest
from django.http import HttpResponse
from django.test import Client
from django.urls import reverse
from toys.models import Toy, ToyImage


@pytest.mark.django_db
def test_toys_list_view(client: Client, fakery_m: Callable[..., Any]) -> None:
    """Тест кверисета toys:index на загрузку связанных с игрушками фото."""
    toy = fakery_m(Toy)()
    fakery_m(ToyImage)(toy=toy)

    response: HttpResponse = client.get(reverse('toys:index'))
    toy = response.context['toys'][0]

    assert isinstance(toy, Toy)
    for image in toy.images.all():
        assert isinstance(image, ToyImage)
