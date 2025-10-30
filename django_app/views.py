from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages
from django.contrib import messages

from .forms import *
from .models import *


def index(request) :
    return render ( request, 'index.html' )


def news(request):
    news = News.objects.all()
    return render ( request, 'news.html', {'news': news} )


def categories(request) :
    categories = Category.objects.all ()
    return render ( request, 'categories.html', {'categories' : categories} )


def categories_with_id(request, category_id) :
    categories = Category.objects.filter ( category_id=category_id )
    return render ( request, 'categories.html', {'categories' : categories} )


def products(request) :
    products = Product.objects.all ()
    categories = Category.objects.all ()
    context = {
        'products' : products,
        'categories' : categories
    }
    return render ( request, 'products.html', context )


def products_by_category(request, category_id) :
    products = Product.objects.filter ( category_id=category_id )
    categories = Category.objects.all ()
    return render ( request, 'products.html', {'products' : products, 'categories' : categories} )


def suppliers(request) :
    suppliers = Supplier.objects.all ()
    return render ( request, 'suppliers.html', {'suppliers' : suppliers} )


def add_news(request) :
    if request.method == 'POST' :
        form = NewsForm ( request.POST, request.FILES )
        if form.is_valid () :
            news = News.objects.create ( **form.cleaned_data )
            return redirect ( 'index' )
    else :
        form = NewsForm ()
    return render ( request, 'add_news.html', {'form' : form} )


def add_category(request) :
    if request.method == 'POST' :
        form = CategoryForm ( request.POST, request.FILES )
        if form.is_valid () :
            category = Category.objects.create ( **form.cleaned_data )
            return redirect ( 'index' )
    else :
        form = CategoryForm ()
    return render ( request, 'add_category.html', {'form' : form} )


def add_product(request) :
    if request.method == 'POST' :
        form = ProductForm ( request.POST, request.FILES )
        if form.is_valid () :
            product = Product.objects.create ( **form.cleaned_data )
            return redirect ( 'index' )
    else :
        form = ProductForm ()
    return render ( request, 'add_product.html', {'form' : form} )


def add_supplier(request) :
    if request.method == 'POST' :
        form = SupplierForm ( request.POST, request.FILES )
        if form.is_valid () :
            supplier = Supplier.objects.create ( **form.cleaned_data )
            return redirect ( 'index' )
    else :
        form = SupplierForm ()
    return render ( request, 'add_supplier.html', {'form' : form} )


def delete_category(request, category_id) :
    if request.method == 'POST' :
        category = get_object_or_404 ( Category, category_id=category_id )
        category_name = Category.category_name
        category.delete ()
        messages.success ( request, f"Category '{category_name}' has been deleted successfully." )
        return redirect ( 'categories' )
    return redirect ( 'categories' )


def delete_product(request, product_id) :
    if request.method == 'POST' :
        product = get_object_or_404 ( Product, product_id=product_id )
        product_name = Product.product_name
        product.delete ()
        messages.success ( request, f"Product '{product_name}' has been deleted successfully." )
        return redirect ( 'products' )
    return redirect ( 'products' )


def delete_supplier(request, supplier_id) :
    if request.method == 'POST' :
        supplier = get_object_or_404 ( Supplier, supplier_id=supplier_id )
        supplier_name = Supplier.contact_name
        supplier.delete ()
        messages.success ( request, f"Supplier '{supplier_name}' has been deleted successfully." )
        return redirect ( 'suppliers' )
    return redirect ( 'suppliers' )


def update_news(request, news_id):
    news = get_object_or_404(News, news_id=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news )
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewsForm(instance=news)
    context = {
        'form': form,
        'news': news
    }
    return render(request, 'update_news.html', context=context)