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

    #LAP7
    path('add/', views.add_books, name='add_books'),
    path('query/', views.simple_query, name='simple_query'),
    path('delete/', views.delete_all, name='delete_all'),
    path('complex/query/', views.complex_query, name='complex_query'),

    #LAP8
    path('lab8/task1/', views.task1, name='task1'),
    path('lab8/task2/', views.task2, name='task2'),
    path('lab8/task3/', views.task3, name='task3'),
    path('lab8/task4/', views.task4, name='task4'),
    path('lab8/task5/', views.task5, name='task5'),
    path('lab8/add_students/', views.add_students),
    path('lab8/task6/', views.task6, name='task6'),
    path('lab8/task7/', views.task7,name='task7'),

]