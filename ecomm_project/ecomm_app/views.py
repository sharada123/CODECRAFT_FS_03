from django.shortcuts import render,redirect,get_object_or_404
from .models import CustomUser,Products,CoverImage,Cart
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
    categories = {
    "Mobile": "assets/images/mobile.jpg",
    "Clothes": "assets/images/clothes.jpg",
    "Books": "assets/images/books.jpg",
    "Kitchen Appliances": "assets/images/kitchen.jpg",
    "Home Decoration": "assets/images/home.jpg",
    "Makeup": "assets/images/makeup.jpg",
    }
    products=Products.objects.all()
    cover_images=CoverImage.objects.all()
    request.session['categories'] =categories
    return render(request, 'home.html',{'products':products,'categories':categories,'covers':cover_images})

def about_us(request):
    return render(request, 'about.html')
def contact_us(request):
    return render(request, 'contact_us.html')
@login_required
def cart(request):
    return render(request, 'cart.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if user already exists BEFORE saving
            if CustomUser.objects.filter(Q(username=username) | Q(email=email)).exists():
                return render(request, 'register.html', {'form': form, 'error': 'Username or Email already exists!'})

            # Check if passwords match
            if password != confirm_password:
                return render(request, 'register.html', {'form': form, 'error': 'Password and Confirm Password did not match!'})

            # Save the user
            user = form.save(commit=False)
            user.set_password(password)  # Hash the password
            user.save()

            return redirect('login')  # Redirect to login after successful registration
        else:
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {'form': RegistrationForm()})


# User Login
def login_view(request):
    print('Login view function called')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password)
           

            if user:
                login(request, user)
            
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password!'})

        else:
            print("Form errors:", form.errors)  # Debugging

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})  # Show login form again

# User Logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def product_detail(request,id):
    product = get_object_or_404(Products, id=id)  
    return render(request, 'product_detail.html',{'product':product})

@login_required
def add_to_cart(request, pid):
    print("Adding function is called")
    uid = request.user

    try:
        product = Products.objects.get(id=pid)
    except Products.DoesNotExist:
        return render(request, 'product_detail.html', {'error_message': 'Product not found'})
    if Cart.objects.filter(Q(pid=product) & Q(uid=uid)).exists():
        return render(request, 'product_detail.html', {'product': product, 'error_message': 'Product is already in the cart'})
    # Add product to cart
    Cart.objects.create(uid=uid, pid=product)
    
    return render(request, 'product_detail.html', {'product': product, 'success_message': 'Product added to cart'})

@login_required
def viewcart(request):
    quantity_dropdown = [1,2,3,4,5,6,7,8,9,10]
    cart_items = Cart.objects.filter(uid=request.user.id).select_related('pid')
    user=CustomUser.objects.get(id=request.user.id)
    print(cart_items)
    return render(request, 'cart.html', {'products': cart_items,'quantity_dropdown': quantity_dropdown,'user':user})
def buy(request):
    return HttpResponse("Bought")
def category_wise_product(request, category_name):
    products = Products.objects.filter(category=category_name)
    categories=request.session.get('categories')
    covers=CoverImage.objects.all()
    if products:
        return render(request, 'home.html', {'products': products,'categories': categories,'covers':covers})
    else:
        return render(request, 'home.html', {'errmsg': "No Products found in this category",'categories': categories,'covers': covers})