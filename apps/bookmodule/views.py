from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm, Book11Form,  BookImageForm
from .models import Book, Booklab9, Publisher

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def insert_books(request):
    #create
    mybook = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)

    #constructor
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save()
    return render(request, 'bookmodule/index.html')


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name})

def index2(request, val1 = 0):
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} 
    return render(request, 'bookmodule/show.html', context)
def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def links(request):
    return render(request, 'links.html')

def formatting(request):
    return render(request, 'formatting.html')

def listing(request):
    return render(request, 'listing.html')

def tables(request):
    return render(request, 'tables.html')


def search_books(request):
    
    Books=[]
    
    if request.method == "POST":

        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # now filter
        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        Books = newBooks

    return render(request, 'bookmodule/search.html', {'books':Books})


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


#LAP8
from django.db.models import Q

def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/LAP8/task1.html', {'books': books})


def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__contains='qu') | Q(author__contains='qu'))
    )
    return render(request, 'bookmodule/LAP8/task2.html', {'books': books})


def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) &
        ~(Q(title__contains='qu') | Q(author__contains='qu'))
    )
    return render(request, 'bookmodule/LAP8/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/LAP8/task4.html', {'books': books})


from django.db.models import Count, Sum, Avg, Max, Min

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/LAP8/task5.html', {'stats': stats})

from .models import Address
def task7(request):
    data = Address.objects.annotate(count=Count('student'))
    return render(request, 'bookmodule/LAP8/task7.html', {'data': data})


 #LAP9
def lab9task1(request):
    books = Booklab9.objects.all()
    total_quantity = sum(book.quantity for book in books) or 1

    for book in books:
        book.percentage = round((book.quantity / total_quantity) * 100, 2)
    return render(request, 'bookmodule/LAP9/task1.html', {'books': books})


def lab9task2(request):
    publishers = Publisher.objects.annotate(
        total_stock=Sum('booklab9__quantity')
    )
    return render(request, 'bookmodule/LAP9/task2.html', {'publishers': publishers})


def lab9task3(request):
    publishers = Publisher.objects.annotate(
        oldest_date=Min('booklab9__pubdate')
    )
    return render(request, 'bookmodule/LAP9/task3.html', {'publishers': publishers})


def lab9task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('booklab9__price'),
        min_price=Min('booklab9__price'),
        max_price=Max('booklab9__price')
    )
    return render(request, 'bookmodule/LAP9/task4.html', {'publishers': publishers})


def lab9task5(request):
    publishers = Publisher.objects.annotate(
        high_rated=Count('booklab9', filter=Q(booklab9__rating__gte=4)
    ),
        quantity = Sum('booklab9__quantity', filter=Q(booklab9__rating__gte=4))
    )
    return render(request, 'bookmodule/LAP9/task5.html', {'publishers': publishers})


def lab9task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books=Count(
            'booklab9',
            filter=Q(
                booklab9__price__gt=50,
                booklab9__quantity__lt=5,
                booklab9__quantity__gte=1
            ) ) )
    return render(request, 'bookmodule/LAP9/task6.html', {'publishers': publishers})


 #LAP10
def list(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/LAP10/part1/list.html', {'books': books})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )

        return redirect('list')

    return render(request, 'bookmodule/LAP10/part1/add.html')

def edit(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']

        book.save()

        return redirect('list')

    return render(request, 'bookmodule/LAP10/part1/edit.html', {'book': book})

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list')

def list2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/LAP10/part2/list2.html', {'books': books})

def add2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list2')
    else:
        form = BookForm()

    return render(request, 'bookmodule/LAP10/part2/add2.html', {'form': form})

def edit2(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/LAP10/part2/edit2.html', {'form': form})

def delete2(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list2')


 #LAP1
def add_book(request):
    if request.method == 'POST':
        form = Book11Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book') 
    else:
        form = Book11Form()

    return render(request, 'bookmodule/LAP11/add_book.html', {'form': form})



def add_book_image(request):
    if request.method == 'POST':
        form = BookImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_book_image')
    else:
        form = BookImageForm()

    return render(request, 'bookmodule/LAP11/add_book_image.html', {'form': form})