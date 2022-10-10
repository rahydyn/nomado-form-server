from django.urls import path, include


v1_patterns = [
    path('auth/', include(('auth.urls', 'auth'))),
    path('users/', include(('users.urls', 'users'))),
    path("forms/", include(("forms.urls", "forms"))),
]


urlpatterns = [
    path('v1/', include((v1_patterns, 'v1'))),
]
