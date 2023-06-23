from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.POST.get('image')
        slug = request.POST.get('image')
        book = Book(title=title, author=author, price=price)
        book.save()
        return redirect('book_list')
    return render(request, 'books/add_book.html')

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = request.session.get('cart', [])
    cart.append(book_id)
    request.session['cart'] = cart
    return redirect('book_list')
