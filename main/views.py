from django.shortcuts import render,redirect
from main.forms import BookForm
from main.models import Book
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse,reverse_lazy


@login_required(login_url=reverse_lazy('main:login'))
def show_main(request):
    books = Book.objects.filter(user = request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'books': books,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)


def create_book(request):
 form = BookForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
    book = form.save(commit=False)
    book.user = request.user
    book.save()
    return redirect('main:show_main')

 context = {'form': form}
 return render(request, "create_book.html", context)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json",data),content_type= "application/json")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request , message= "Your account has been successfully created!")
            return redirect("main:login")
        
    context = {"form" : form}

    return render(request, "register.html" , context)

def login_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username= username , password= password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')

    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_css(request):
    return render(request,"tutor.html")

def edit_book(request, id):
    # Get book berdasarkan ID
    book = Book.objects.get(pk = id)

    # Set book sebagai instance dari form
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_book.html", context)

def delete_book(request, id):
    # Get data berdasarkan ID
    book = Book.objects.get(pk = id)
    # Hapus data
    book.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
