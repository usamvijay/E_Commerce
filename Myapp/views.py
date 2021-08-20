from django.contrib.auth import decorators
from django.core import paginator
from django.db.models.base import Model
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.http import request
from Myapp import models
from .models import  User_data, products,cart
from .models import Catagory
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.db import connection
from django.contrib.auth.decorators import login_required
from Myapp.middleware import auth_middleware
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from hashlib import md5
from six import ensure_binary


# Create your views here.


# SITE VIEWS HARE.....

def Register(request):
    try:
        msg =   request.session['msg']
        del request.session['msg']
    except:
        msg =   ''
    
    return render(request, 'Register.html', {'msg':msg})

# Cart Page view...
def cart(request):

    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')

#Index page view hare..

def index(request):
    product=products.objects.all().order_by('-id')
    catagory=Catagory.objects.all()
    
    
    context={
        'product':product,
        'catagory':catagory,
        
    
    }

    return render(request, 'index.html',context)


def shop(request):
    product=products.objects.all().order_by('-id')
    catagory=Catagory.objects.all()
    
    
    context={
        'product':product,
        'catagory':catagory,
        
    
    }

    return render(request, 'shop.html',context)


def vijay(request,id):
    product=products.objects.all().order_by('-id')
    catagory=Catagory.objects.all()
    product=products.objects.filter(cat_id=id)
    context={
        'product':product,
        'product':product,
        'catagory':catagory,
    }
    return render(request,'index.html', context)



# user change password....
def change_password(request,id):
    if request.method=='POST':

        psw=request.POST.get('password1')

        Cpsw=request.POST.get('password2')
        if psw==Cpsw:
           user=User_data.objects.get(id=id)

           user.password=psw
           user.Cpassword=Cpsw
           user.save()
           messages.info(request, "You're Password Has changed Succussefully...")
           return redirect('/profile')
        else:
            messages.info(request, "Password & Confirm Password Must Be Same...")
            return render(request, 'change-password.html')

    else:
        user=User_data.objects.get(id=id)
        context={
         'user':user
        }



    return render(request, 'change-password.html',context)

# user update profiel hare..
def update_profile(request,id):
    if request.method=='POST':

        firstname=request.POST.get('firstname')

        lastname=request.POST.get('lastname')

        email=request.POST.get('email')

        mobile=request.POST.get('mobile')

        user=User_data.objects.get(id=id)

        user.firstname=firstname
        user.lastname=lastname
        user.email=email
        user.contact=mobile
        user.save()
        return redirect('/profile')

        
    else:
        user=User_data.objects.get(id=id)
        context={
            'user':user
        }
    messages.info(request, "You're Profile Has Updated Succussefully...")
    return render(request, 'update_profile.html',context)


# user register hare
def user_data(request):
    if request.method=='POST':
        # firstname=request.POST['firstname']
        # lastname=request.POST['lastname']
        # email=request.POST['email']
        # mobile=request.POST['mobile']
        # password=request.POST['password1']
        # Cpassword=request.POST['password2']
        # if password==Cpassword:
        #   if User_data.objects.filter(email=email).exists():
        #       messages.info(request, "Email Address Has Alredy Registered...")
        #       return redirect("/Register")
        #   else:
        #     user_data=User_data(firstname=firstname, lastname=lastname, email=email, contact=mobile, password=password, Cpassword=Cpassword)
        #     user_data.save()
        #     messages.info(request, "You're Registered Successfully...")
        #     return redirect("/Register")
        # else:
        #  messages.info(request, "Password & Confirm Password Must Be Same...")

        # return redirect('/Register')
        
        if models.User_data.objects.filter(email=request.POST['email']).exists():
            request.session['msg'] = "Email Already Exists"
            return HttpResponseRedirect("/Register")
        elif md5(ensure_binary(request.POST['password1'])).hexdigest() == md5(ensure_binary(request.POST['password2'])).hexdigest():
            user = models.User_data()
            user.firstname  =   request.POST['firstname']
            user.lastname   =   request.POST['lastname']
            user.email      =   request.POST['email']
            user.contact    =   request.POST['mobile']
            user.password   =   md5(ensure_binary(request.POST['password1'])).hexdigest()
            user.save()
            request.session['msg'] = "Registered Successfully.....!"
            return HttpResponseRedirect("/Register")
        else:
            request.session['msg'] = "New and Confirm Password are Not Matching"
            return HttpResponseRedirect("/Register")
# user login.....
def login_data(request):
    if request.method=='POST':
        try:
            userdata=User_data.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['email']=userdata.email
            messages.info(request, "You're Successfully Loged In...")

            return redirect('/index')
        except User_data.DoesNotExist as e:
            messages.info(request, 'Invalide Email Or Password...')
    return redirect('/login_view')

#Login page view..
def login_view(request):
    return render(request, 'login.html')


#user_logout hare...
def logout(request):
    # auth.logout(request)
    try:
        del request.session['email']
    except:
        pass
    return redirect('/index')

# user_profile page...
def profile(request):
    user=request.session['email']
    profile=User_data.objects.get(email=user)
    user_id=profile.id
    print(user_id)
    
    
    context={
        'user':user,
        'usr':profile
    }
    
    
    return render(request, 'user.profile.html',context)

# Site Product Details Page hare...
def product_details(request,id):
    
    producting=products.objects.filter(id=id)
    context={
        'producting':producting
    }
   
    return render(request, 'product-details.html', context)




#    ..........////ADMIN VIEWS//////................



# List of Registerd users in Admin Dashboard page hare..


def Custumers(request):
    user=User_data.objects.all()
    context={
        'user':user
    }
    return render(request, 'admin/Costumers.html',context)

# ////......catagorries......////

#Show Catagories List Hare....
def Catagories(request):
    catagory=Catagory.objects.all()
    context={
        'catagory':catagory
    }
    
    return render(request, 'admin/Catagories.html',context)

# admin edit catagories Hare...
def edit_catagory(request,id):
    if request.method=='POST':
        cat=request.POST.get('cat')
        catgorys=Catagory.objects.get(id=id)

        catgorys.Cat=cat
        catgorys.save()
        return redirect('/Catagories')
    else:

      catagory=Catagory.objects.get(id=id)

      context={
            'cat':catagory
        }


      return render(request, 'admin/update_catagory.html',context)

# Admin Add Catagories hare....

def add_Catagories(request):
    
    if request.method =="POST":
        if request.POST.get('hello'):

          catgory= Catagory()

          catgory.Cat=request.POST.get('hello')
          catgory.save()

       
        return redirect('/Catagories')

# admin delete Catagories hare...
def delete_catagory(request,id):
   catagory=Catagory.objects.get(id=id)
   catagory.delete()
   return redirect("/Catagories")


# /////....Products...///



def Products(request):
    catgory=Catagory.objects.all()
    product=products.objects.all()

    paginator=Paginator(product, 10)
    page=request.GET.get('page')
    product=paginator.get_page(page)

    context={
        'catagory':catgory,
        'product':product,   }


    return render(request, 'admin/Products.html',context)

# admin add_products hare...

def adding_Products(request):
    if request.method == 'POST' and request.FILES['image']:
        Cat_id=request.POST['cat_id']

        title=request.POST['name']

        image=request.FILES['image']

        Offer_price=request.POST['offer-price']

        final_price=request.POST['final_price']

        discription=request.POST['description']

        product=products(cat_id=Cat_id, title=title, image=image,offer_price=Offer_price,final_price=final_price,Description=discription)
        product.save()
        return redirect('/Products')
    else:
        return redirect('/Products')


# admin edit and update products Hare...

def update_products(request,id):
    cat=Catagory.objects.all()
    if request.method=='POST' and request.FILES['image']:

        Cat=request.POST.get('cat_id')

        title=request.POST.get('name')

        image=request.FILES.get('image')

        Offer_price=request.POST.get('offer-price')

        final_price=request.POST.get('final_price')

        discription=request.POST.get('description')

        product=products.objects.get(id=id)

        
        product.title=title
        product.image=image
        product.Offer_price=Offer_price
        product.final_price=final_price
        product.discription=discription
        product.save()
        return redirect('/Products')
    else:

      product=products.objects.get(id=id)

      context={
            'cat':cat,
            'product':product
        }


      return render(request, 'admin/update_products.html',context)

# admin delete Products Hare....

def delete_products(request,id):
    
   catagory=products.objects.get(id=id)
   catagory.delete()
   return redirect("/Products")







    