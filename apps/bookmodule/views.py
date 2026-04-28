from django.shortcuts import render # type: ignore
#LAP7
from django.http import HttpResponse # type: ignore
from .models import Book , Student, Address,Publisher

#LAP8
from django.db.models import Count, Sum, Avg, Max, Min ,Q # type: ignore
from django.http import HttpResponse # type: ignore
from django.db.models import Count ,Q# type: ignore

#LAP9
def task1_L9(request):  
    total_books = Book.objects.count()
    
    books = Book.objects.select_related('publisher').prefetch_related('authors').all()
    
    for book in books:
        if total_books > 0:
            book.availability_percent = (book.quantity / total_books) * 100
        else:
            book.availability_percent = 0
        
        if book.availability_percent >= 30:
            book.stock_status = "High Stock"
        elif book.availability_percent >= 10:
            book.stock_status = "Medium Stock"
        elif book.availability_percent >= 1:
            book.stock_status = "Low Stock"
        else:
            book.stock_status = "Very Rare"
    
    context = {
        'books': books,
        'total_books': total_books,
        'total_quantity': Book.objects.aggregate(total=Sum('quantity'))['total'] or 0
    }
    
    return render(request, 'bookmodule/task1_L9.html', context)

def task2_L9(request):
    
    publishers = Publisher.objects.annotate(
        total_stock=Sum('book__quantity')
    ).order_by('-total_stock')  
    
    for publisher in publishers:
        if publisher.total_stock is None:
            publisher.total_stock = 0
    
    total_books_all = Book.objects.count()
    total_stock_all = Book.objects.aggregate(total=Sum('quantity'))['total'] or 0
    publishers_with_books = publishers.filter(total_stock__gt=0).count()
    publishers_without_books = publishers.filter(total_stock=0).count()
    
    context = {
        'publishers': publishers,
        'total_books_all': total_books_all,
        'total_stock_all': total_stock_all,
        'publishers_with_books': publishers_with_books,
        'publishers_without_books': publishers_without_books,
    }
    
    return render(request, 'bookmodule/task2_L9.html', context)

def task3_L9(request):
    
    publishers = Publisher.objects.annotate(
        oldest_date=Min('book__pubdate')
    )
    
    publishers_with_oldest_book = []
    
    for publisher in publishers:
        if publisher.oldest_date:
            oldest_book = Book.objects.filter(
                publisher=publisher,
                pubdate=publisher.oldest_date
            ).first()
        else:
            oldest_book = None
            publisher.oldest_date = None
        
        publishers_with_oldest_book.append({
            'publisher': publisher,
            'oldest_book': oldest_book,
            'oldest_date': publisher.oldest_date,
        })
    
    publishers_with_books = Publisher.objects.filter(book__isnull=False).distinct().count()
    publishers_without_books = Publisher.objects.filter(book__isnull=True).count()
    
    context = {
        'publishers_data': publishers_with_oldest_book,
        'total_publishers': Publisher.objects.count(),
        'publishers_with_books': publishers_with_books,
        'publishers_without_books': publishers_without_books,
    }
    
    return render(request, 'bookmodule/task3_L9.html', context)

def task4_L9(request):
      
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    ).order_by('name')
    
    for publisher in publishers:
        if publisher.avg_price is None:
            publisher.avg_price = 0
            publisher.min_price = 0
            publisher.max_price = 0
    
    total_publishers = Publisher.objects.count()
    publishers_with_books = publishers.filter(avg_price__gt=0).count()
    publishers_without_books = total_publishers - publishers_with_books
    
    context = {
        'publishers': publishers,
        'total_publishers': total_publishers,
        'publishers_with_books': publishers_with_books,
        'publishers_without_books': publishers_without_books,
    }
    
    return render(request, 'bookmodule/task4_L9.html', context)


def task5_L9(request):
   
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4))
    ).order_by('-high_rated_count')  # Publisher with most high-rated books first
    
    for publisher in publishers:
        publisher.total_books = publisher.book_set.count()
        if publisher.total_books > 0:
            publisher.high_rated_percentage = (publisher.high_rated_count / publisher.total_books) * 100
        else:
            publisher.high_rated_percentage = 0
    
    total_high_rated_books = Book.objects.filter(rating__gte=4).count()
    total_books = Book.objects.count()
    publishers_with_high_rated = publishers.filter(high_rated_count__gt=0).count()
    
    context = {
        'publishers': publishers,
        'total_high_rated_books': total_high_rated_books,
        'total_books': total_books,
        'publishers_with_high_rated': publishers_with_high_rated,
    }
    
    return render(request, 'bookmodule/task5_L9.html', context)

def task6_L9(request):
   
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'book', 
            filter=Q(
                book__price__gt=50,
                book__quantity__lt=5,
                book__quantity__gte=1
            )
        )
    ).order_by('-filtered_books_count')
    
    publishers_with_details = []
    for publisher in publishers:
        filtered_books = Book.objects.filter(
            publisher=publisher,
            price__gt=50,
            quantity__lt=5,
            quantity__gte=1
        )
        
        publishers_with_details.append({
            'publisher': publisher,
            'count': publisher.filtered_books_count,
            'books': filtered_books,
            'total_books': publisher.book_set.count(),
        })
    
    total_matching_books = Book.objects.filter(
        price__gt=50,
        quantity__lt=5,
        quantity__gte=1
    ).count()
    
    publishers_with_matches = publishers.filter(filtered_books_count__gt=0).count()
    
    context = {
        'publishers_data': publishers_with_details,
        'total_matching_books': total_matching_books,
        'publishers_with_matches': publishers_with_matches,
        'total_publishers': Publisher.objects.count(),
    }
    
    return render(request, 'bookmodule/task6_L9.html', context)






#LAP8
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) &
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def add_students(request):
    # Cities
    c1 = Address.objects.create(city="Riyadh")
    c2 = Address.objects.create(city="Jeddah")

    # Students
    Student.objects.create(name="Ali", age=22, address=c1)
    Student.objects.create(name="Sara", age=21, address=c1)
    Student.objects.create(name="Fahad", age=23, address=c2)

    return HttpResponse("Students added successfully")

def task6(request):
    students = Student.objects.select_related('address').all()
    return render(request, 'bookmodule/task6.html', {'students': students})

def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})


#LAP7

def add_books(request):
    b1 = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.00, edition=3)
    b1.save()

    b2 = Book.objects.create(title='Reversing: Secrets of Reverse Engineer', author='E. Eilam', price=97.00, edition=2)

    b3 = Book.objects.create(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4)

    b4 = Book.objects.create(title='Data and AI', author='Ali', price=150.00, edition=3)

    b5 = Book.objects.create(title='Cheap Book', author='Test', price=50.00, edition=3)

    b6 = Book.objects.create(title='Quantum Computing Basics', author='John Quantum', price=200.00, edition=5)

    b7 = Book.objects.create(title='Quick Python Guide', author='Ali Qureshi', price=70.00, edition=7)


    return HttpResponse("Books added successfully")

def simple_query(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': books})

def delete_all(request):
    Book.objects.all().delete()
    return HttpResponse("All books deleted")

def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')

#LAP6
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def search(request):

    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and keyword in item['title'].lower():
                contained = True
            if not contained and isAuthor and keyword in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')








#LAO5
def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')



#LAP4
def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")