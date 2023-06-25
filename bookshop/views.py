from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse

from bookshop.forms import AddBookForm
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{'books' : books})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)  

        if form.is_valid():
            form.save()  
            return redirect(reverse('bookshop:book_list'))

    else:
        form = AddBookForm()  

    return render(request, 'add_books.html', {'form': form})


def add_to_cart(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        product_id = request.POST.get('product_id')

        if product_id:
            if 'cart' in request.session:
                request.session['cart'].append(product_id)
            else:
                request.session['cart'] = [product_id]

            cart_count = len(request.session.get('cart', []))

            response_data = {
                'cart_count': cart_count,
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid product_id'})

    return JsonResponse({'error': 'Invalid request'})




def cart(request):
    cart_items = []
    if 'cart' in request.session:
        cart_ids = request.session['cart']
        cart_items = Book.objects.filter(id__in=cart_ids)
    return render(request, 'cart.html', {'cart_items': cart_items})

