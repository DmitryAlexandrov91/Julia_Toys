from typing import Any, Callable

import pytest
from django.db import models
from django_fakery.faker_factory import Factory


@pytest.fixture
def fakery_m(
    fakery: Factory,
    # monkeypatch: pytest.MonkeyPatch,
) -> Callable[..., Any]:
    """Фабрика генерации объектов django модели."""
    # # TODO: remove after https://github.com/fcurella/django-fakery/pull/77
    # # will be merged.
    # monkeypatch.setitem(fakery.field_names, 'full_name', ('name', (), {}))

    def factory(model_type: models.Model) -> Any:
        return fakery.m(  # type: ignore[call-overload, no-any-return]
            model_type,
        )

    return factory
