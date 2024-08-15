from django.shortcuts import render,redirect
from main.forms import BookForm
from main.models import Book

def show_main(request):
    books = Book.objects.all()

    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A',
        'books': books
    }

    return render(request, "main.html", context)

def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_book.html", context)