from django.shortcuts import render # type: ignore
#LAP7
from django.http import HttpResponse # type: ignore
from .models import Book , Student, Address

#LAP8
from django.db.models import Q # type: ignore
from django.db.models import Count, Sum, Avg, Max, Min # type: ignore
from django.http import HttpResponse # type: ignore
from django.db.models import Count # type: ignore

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