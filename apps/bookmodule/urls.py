from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('html5/links', views.links),
    path('html5/text/formatting', views.formatting),
    path('html5/listing', views.listing),
    path('html5/tables', views.tables),
]