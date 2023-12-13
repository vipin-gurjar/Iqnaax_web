from django.shortcuts import render,redirect
from .models import Steam_Product,Lab_Setup,Cart
from account.models import Customer
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def shop(request):
    return render(request, 'myapp/shop.html')

def filter_products(request):
    products = Steam_Product.objects.all()
    sort = request.GET.get('sort', 'default')  
    if sort == 'title_az':
        products = products.order_by('title')
    elif sort == 'title_za':
        products = products.order_by('-title')
    elif sort == 'price_low_to_high':
        products = products.order_by('discounted_price')
    elif sort == 'price_high_to_low':
        products = products.order_by('-discounted_price')
        
    context = {'products': products}
    return render(request, 'myapp/product_list.html', context)

def lab_product(request):
    products = Lab_Setup.objects.all()
    sort = request.GET.get('sort', 'default')  
    if sort == 'title_az':
        products = products.order_by('title')
    elif sort == 'title_za':
        products = products.order_by('-title')
    elif sort == 'price_low_to_high':
        products = products.order_by('discounted_price')
    elif sort == 'price_high_to_low':
        products = products.order_by('-discounted_price')
        
    context = {'products': products}
    return render(request, 'myapp/labproducts.html', context)


class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        prod = Steam_Product.objects.get(pk=pk)
        products = Steam_Product.objects.all()
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=prod .id) & Q(user=request.user)).exists()
            
        return render(request, 'myapp/productDetails.html', {'prod': prod,'products': products, 'item_already_in_cart': item_already_in_cart,'totalitem':totalitem})
    
class LabProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        prod = Lab_Setup.objects.get(pk=pk)
        products = Lab_Setup.objects.all()
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=prod .id) & Q(user=request.user)).exists()
            
        return render(request, 'myapp/labproductsdetails.html', {'prod': prod,'products': products, 'item_already_in_cart': item_already_in_cart,'totalitem':totalitem})
    
@login_required
def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('prod_id')
    product = Steam_Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('cart')

@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user=request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
   

        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount 
            return render(request, 'myapp/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount,'totalitem':totalitem})
        else:
            return render(request, 'myapp/empty.html')

def empty(request):
    return render(request, 'myapp/empty.html')

@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        # shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
               

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':amount 
            # + shipping_amount
            }
        return JsonResponse(data)
    
@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        # shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
              

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':amount 
            # + shipping_amount
            }
        return JsonResponse(data)

@login_required 
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        # shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
             

        data = {
            'amount': amount,
            'totalamount':amount 
            # + shipping_amount
            }
        return JsonResponse(data)
    

# @login_required 
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    # shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount=amount 
        # + shipping_amount
    return render(request, 'myapp/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})
