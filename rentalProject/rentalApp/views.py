from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .form import UserRegisterForm,ProfileForm,PropertyUpload
from .models import Profile,Property,PropertyImage, PerportyType, Contact
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    properties = Property.objects.prefetch_related('images').all()
    rent = properties.filter(category_id=1)
    rent_paginator = Paginator(rent, 3) #show 3 properties per page
    page_number = request.GET.get('page')
    page_obj = rent_paginator.get_page(page_number)
    total = page_obj.paginator.num_pages

    sale = properties.filter(category_id=2)
    sale_paginator = Paginator(sale, 3)  # Show 3 properties per page
    page_number = request.GET.get('page2')
    page_obj2 = sale_paginator.get_page(page_number)
    total2 = page_obj2.paginator.num_pages

    if request.method == "POST":
        location = request.POST['location']
        if Property.objects.filter(location__iexact=location).exists():
            return redirect('for_rent')
        else:
            return redirect('for_sale')

    context = {
        'page_obj': page_obj,
        'page_obj2': page_obj2,
        'num': [i+1 for i in range(total)],
        'num2': [i+1 for i in range(total2)],
    }
    return render(request, 'rentalApp/index.html',context)

@login_required(login_url='login')
def about(request):
    return render(request,'rentalApp/about.html')

def for_rent(request):
    category = PerportyType.objects.all()
    cateid = request.GET.get("perportyType")
    if cateid:
        property_cate = Property.objects.filter(perportyType=cateid)
    else:
        property_cate = Property.objects.all()

    properties = Property.objects.prefetch_related('images').all()
    rent = properties.filter(category_id=1)
    rent_paginator = Paginator(rent, 6)  # Show 6 properties per page
    page_number = request.GET.get('page')
    page_obj = rent_paginator.get_page(page_number)
    total = page_obj.paginator.num_pages

    context = {
        'properties':property_cate,
        'category':category,
        'page_obj': page_obj,
        'num': [i+1 for i in range(total)],
    }
    return render(request,'rentalApp/for_rent.html',context)

def for_sale(request):
    category = PerportyType.objects.all()
    cateid = request.GET.get("perportyType")
    if cateid:
        property_cate = Property.objects.filter(perportyType=cateid)
    else:
        property_cate = Property.objects.all()
    properties = Property.objects.all()
    sale = properties.filter(category_id=2)
    sale_paginator = Paginator(sale, 6)  # Show 6 properties per page
    page_number = request.GET.get('page2')
    page_obj2 = sale_paginator.get_page(page_number)
    total2 = page_obj2.paginator.num_pages
    context = {
        'properties':property_cate,
        'category':category,
        'page_obj2': page_obj2,
        'num2': [i+1 for i in range(total2)],
    }
    return render(request,'rentalApp/for_sale.html',context)

def services(request):
    return render(request,'rentalApp/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact.objects.create(name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request,'Thank You!')
        return redirect('index')
    return render(request,'rentalApp/contact.html')

def rent_details(request,id):
    property = get_object_or_404(Property, id=id)
    return render(request,'rentalApp/rent_details.html',{'property':property})

def terms(request):
    return render(request,'rentalApp/terms.html')

def privacy(request):
    return render(request,'rentalApp/privacy.html')


@login_required(login_url='login')
def upload_property(request):
    if request.method == 'POST':
        form = PropertyUpload(request.POST)
        images = request.FILES.getlist('images')  # get multiple files

        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()

            for img in images:
                PropertyImage.objects.create(property=property, image=img)

            return redirect('myproperty')
    else:
        form = PropertyUpload()

    return render(request, 'rentalApp/upload_property.html', {'form': form})



@login_required(login_url='login')
def my_property(request):
    properties = Property.objects.filter(user=request.user).prefetch_related('images')
    return render(request, 'profile/my_property.html', {'properties': properties})

def property_delete(request, id):
    property_obj = get_object_or_404(Property, id=id)
    if request.user == property_obj.user:  # authorization check, if needed
        property_obj.delete()
    return redirect('myproperty')

def property_edit(request, id):
    property_obj = get_object_or_404(Property, id=id)

    if request.user != property_obj.user:
        return redirect('myproperty')

    if request.method == 'POST':
        form = PropertyUpload(request.POST, request.FILES, instance=property_obj)
        images = request.FILES.getlist('images')

        if form.is_valid():
            property_instance = form.save()

            # Save each uploaded image
            for image in images:
                PropertyImage.objects.create(property=property_instance, image=image)

            return redirect('myproperty')
    else:
        form = PropertyUpload(instance=property_obj)

    return render(request, 'profile/property_edit.html', {
        'form': form,
        'property': property_obj,
    })
'''
#######################################################
#######################################################
################ auth section #########################
#######################################################
#######################################################
'''

def register(request):
    if request.method == 'POST':
        role = request.POST.get('mySelect')  # form bata role aayo
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('register')

            # create user
            user = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=username,
                email=email,
                password=password
            )

            # fetch auto-created profile and update role
            user.refresh_from_db()  # yo important cha, natra profile load hudaina
            user.profile.role = role
            user.profile.save()

            messages.success(request, 'Your registration was successful!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

    return render(request, 'auth/register.html')





def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Username is not registered!')
            return redirect('login')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            next = request.POST.get('next','')
            return redirect(next if next else 'index')
        else:
            messages.error(request,'Invalid password')
            return redirect('login')
    next = request.GET.get('next','')

    return render(request,'auth/login.html',{'next':next})

def log_out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    print(request.user.profile.role) 
    return render(request,'profile/profile.html')

@login_required(login_url='login')
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)  # This line is crucial for GET requests

    context = {
        'form': form
    }
    return render(request, 'profile/update_profile.html', context)

def change_password(request):
    forms = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        forms = PasswordChangeForm(user=request.user,data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    return render(request,'profile/change_password.html',{'forms':forms})
