from django.shortcuts import render # type: ignore

#LAP7
from django.http import HttpResponse # type: ignore
from .models import Book

def add_books(request):
    b1 = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.00, edition=3)
    b1.save()

    b2 = Book.objects.create(title='Reversing: Secrets of Reverse Engineer', author='E. Eilam', price=97.00, edition=2)

    b3 = Book.objects.create(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4)

    b4 = Book.objects.create(title='Data and AI', author='Ali', price=150.00, edition=3)

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