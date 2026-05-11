from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product



def shop(request):
    categories = Category.objects.all()
    return render(request, 'shop/shop.html', {'categories': categories})

def category_view(request, slug=None):
    p = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=p).order_by('-uploaded_at')
    context = {
        'category': p,
        'products': products
    }
    return render(request, 'shop/index.html', context)

def product_view(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'shop/product.html', context)

@login_required
def toggle_like(request, slug=None):
    product = get_object_or_404(Product, slug=slug)

    if request.user in product.likes.all():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)

    return redirect('product_view', slug=product.slug)

@login_required
def wishlist(request):
    products = request.user.products.all()
    return render(request, 'shop/wishlist.html', {'products': products})

