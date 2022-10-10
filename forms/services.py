from typing import Tuple

from .models import Form

def form_create(title, user, formId, **extra_fields) -> Form:

    form = Form(title=title, user=user, formId=formId, **extra_fields)

    form.full_clean()
    form.save()

    return form

def form_get_or_create(*, title: str, user: str formId: str, **extra_data) -> Tuple[Form, bool]:
    form = Form.objects.filter(formId=formId, user=user).first()

    if form:
        return form, False

    return form_create(title=title, user=user, formId=formId **extra_data), True
