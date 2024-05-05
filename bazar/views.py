from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')  
         
        else:
            
            messages.error(request, 'Invalid username or password.')
            return redirect('signin')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        user = User.objects.create_user(username=username, email=email, password=password)

        
        request.session['signup_username'] = username
        request.session['signup_email'] = email
        request.session['signup_password'] = password

        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            auth_login(request, user)
            messages.success(request, 'You have successfully signed up!')
            return redirect('signin')  

    return render(request, 'signup.html')

@login_required(login_url='signin')
def profile(request):
    order_items = Order.objects.filter(user=request.user)
    total_amount = sum(item.product.price * item.quantity for item in order_items)
    context = {'order_items': order_items, 'total_amount': total_amount}
    return render(request, 'profile.html', context)

def logout(request):
    django_logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('home')


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def productdetails(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'productdetails.html', context)

@login_required(login_url='signin')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        
        cart_item.quantity += 1
    else:
        
        cart_item.quantity = 1
    
    cart_item.save()
    
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item = get_object_or_404(Cart, product=product)
    cart_item.delete()
    return redirect('view_cart')

def view_cart(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def update_quantity(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item = get_object_or_404(Cart, product=product)
    if 'action' in request.POST:
        action = request.POST['action']
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
        cart_item.save()
    return redirect('view_cart')


@login_required
def proceed_to_checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        if item.product.stock >= item.quantity:
            item.product.stock -= item.quantity
            item.product.save()
        else:
            
            # You can add your custom logic here
            pass
    
    
    order = Order.objects.create(user=request.user, product=item.product, quantity=item.quantity, total_price=item.product.price * item.quantity)
    
    
    cart_items.delete()
    
    return redirect('checkout') 

def checkout(request):
    return render(request, 'checkout.html')



@login_required
def pay_now(request):
    
    user = request.user
    order_items = Order.objects.filter(user=user)  
    total_amount = sum(item.product.price * item.quantity for item in order_items)

    
    subject = 'Order Confirmation'
    email_template_name = 'confirmationemail.html'
    context = {
        'user': user,
        'order_items': order_items,
        'total_amount': total_amount,
    }
    email_content = render_to_string(email_template_name, context)

    
    send_mail(
        subject,
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=email_content
    )

    
    return redirect('orderconfirm')


def orderconfirm(request):
    return render(request, 'orderconfirm.html')