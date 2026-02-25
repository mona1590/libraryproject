from django.urls import path # type: ignore
from . import views # type: ignore
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
]
