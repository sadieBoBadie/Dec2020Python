from django.shortcuts import render, HttpResponse
from .models import Author, Book
# Create your views here.
def index(request):

    my_book = Book.objects.get(id=2)
    my_book.title = "Hello World"
    my_book.save()

    new_book = Book.objects.create(
        title="The Water Dancer",
        description="A book about telepathy and antebellum south",
        author=Author.objects.get(id=2)
        )
    
    context = {
        "authors": Author.objects.all()
    }
    # first_author = Author.objects.first()
    # first_author_books = first_author.books.all()

    return render(request, "index.html", context)
