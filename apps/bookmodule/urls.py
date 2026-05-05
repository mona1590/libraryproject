from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    path('html5/links', views.links),
    path('html5/text/formatting', views.formatting),
    path('html5/listing', views.listing),
    path('html5/tables', views.tables),
    
    path('search', views.search_books),
    
    path('insert', views.insert_books),

    path('simple/query', views.simple_query),
    path('complex/query', views.complex_query),


    #LAP8
    path('LAP8/task1', views.task1),
    path('LAP8/task2', views.task2),
    path('LAP8/task3', views.task3),
    path('LAP8/task4', views.task4),
    path('LAP8/task5', views.task5),
    path('LAP8/task7', views.task7),
    
    
    #LAP9
    path('LAP9/task1', views.lab9task1),
    path('LAP9/task2', views.lab9task2),
    path('LAP9/task3', views.lab9task3),
    path('LAP9/task4', views.lab9task4),
    path('LAP9/task5', views.lab9task5),
    path('LAP9/task6', views.lab9task6),
    
 
    #LAP10
    path('LAP10_part1/list', views.list, name='list'),
    path('LAP10_part1/add', views.add, name='add'),
    path('LAP10_part1/edit/<int:id>', views.edit, name='edit'),
    path('LAP10_part1/delete/<int:id>', views.delete, name='delete'),
    
    path('LAP10_part2/list2', views.list2, name='list2'),
    path('LAP10_part2/add2', views.add2, name='add2'),
    path('LAP10_part2/edit2/<int:id>', views.edit2, name='edit2'),
    path('LAP10_part2/delete2/<int:id>', views.delete2, name='delete2'),
    
    #LAP11
    path('LAP11/add_book', views.add_book, name='add_book'),
    path('LAP11/add_book_image/', views.add_book_image, name='add_book_image'),

]
