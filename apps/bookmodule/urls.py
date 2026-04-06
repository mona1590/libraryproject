from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('', views.index, name='books.index'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
    path('aboutus/', views.aboutus, name='books.aboutus'),

    # Lab 5
    path('html5/links/', views.links, name='links'),
    path('html5/text/formatting/', views.formatting, name='formatting'),
    path('html5/listing/', views.listing, name='listing'),
    path('html5/tables/', views.tables, name='tables'),

    # Lab 6
    path('search/', views.search, name='search'),
]