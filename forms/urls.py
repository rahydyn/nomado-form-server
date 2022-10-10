from django.urls import path

from forms.apis import FormListApi, FormInitApi, FormDetailApi


urlpatterns = [
    # GET
    path('list/', FormListApi.as_view(), name='list'),
    # GET
    path("list/<str:pk>", FormDetailApi.as_view(), name="detail"),
    # POST
    path('init/', FormInitApi.as_view(), name='init'),
]
