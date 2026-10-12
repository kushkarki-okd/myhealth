from django.urls import path
from diseases.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("a/",predictdiseases.as_view(), name="predictdiseases"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )