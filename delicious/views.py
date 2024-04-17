from django.core import paginator
from django.shortcuts import render,redirect
from .models import Order,Cart,UserDetails,FoodVlogs,ExecutiveDetails,Advertisements
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import JsonResponse
from django.db.models.query_utils import Q



# Create your views here.
def base(request):
    return render(request,'delicious/base.html')

def home(request):
    veg = Order.objects.filter(category='V')
    nonveg = Order.objects.filter(category='N')
    desserts = Order.objects.filter(category='D')
    return render(request,'delicious/home.html',{'veg':veg,'nonveg':nonveg,'desserts':desserts})

def items(request,pk):
    item_info = Order.objects.get(pk=pk)
    return render(request,'delicious/items.html',{'item_info':item_info})

def menu(request,data=None):
    if data==None:
        menu_info = Order.objects.all()
    elif data=='V':
        menu_info = Order.objects.filter(category='V')
    elif data=='Rice' or data=='Starter':
        menu_info = Order.objects.filter(type=data)
    elif data=='N':
        menu_info = Order.objects.filter(category='N')
    elif data=='D':
        menu_info = Order.objects.filter(category='D')
    elif data=='below':
        menu_info = Order.objects.all().filter(offer_price__lt=500)
    elif data=='above':
        menu_info = Order.objects.all().filter(offer_price__gt=500)

        
    return render(request,'delicious/menu.html',{'menu_info':menu_info})
    

def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product = Order.objects.get(id=product_id)
    Cart(product=product).save()
    return redirect('/cart')

def show_cart(request):
    cart = Cart.objects.all()
    amount = 0.0
    shipping_amount = 70
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() ]
    if cart_product:
        for p in cart_product:
            tempamount = p.quantity * int(p.product.offer_price)
            amount += tempamount
            totalamount = amount+shipping_amount
        return render(request, 'delicious/add_to_cart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
    else:
        return render(request,'delicious/emptycart.html')

def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id))
        
        c.delete()
        amount = 0.0
        shipping_amount = 70
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all()]
        
        for p in cart_product:
            tempamount = p.quantity * int(p.product.offer_price)
            amount += tempamount
            

        data={
            
            'amount':amount,
            'totalamount':amount+shipping_amount

            }

        return JsonResponse(data)


def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all()]
        
        for p in cart_product:
            tempamount = p.quantity * int(p.product.offer_price)
            amount += tempamount
           

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount

            }

        return JsonResponse(data)

def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all()]
        
        for p in cart_product:
            tempamount = p.quantity * int(p.product.offer_price)
            amount += tempamount
            

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount

            }

        return JsonResponse(data)
    
def register(request):
       if request.method == "POST":
        

            obj = UserDetails()
            obj.first_name = request.POST.get('first_name')
            obj.last_name = request.POST.get('last_name')
            obj.username = request.POST.get('username')
            obj.password1 = request.POST.get('password1')
            obj.password2 = request.POST.get('password2')

            if obj.password1 == obj.password2:
                if UserDetails.objects.filter(username=obj.username).exists():
                    return render(request,'delicious/registration.html',{'msg':' username is already taken'})

                else:
                    obj.save()
                    return render(request,'delicious/successreg.html')
            else:
            
                return render(request,'delicious/registration.html',{'error':'recheck your password'})

       else:
          return render(request,'delicious/registration.html')

def login(request):
    
    if request.method=="POST":
        
        try:

           user_data = UserDetails.objects.get(username=request.POST.get("username"),password1=request.POST.get("password1"))
        
        
           request.session['userform']=user_data.username
           
           return render(request, 'delicious/success.html', {'user_data':user_data})
        except:
            return render(request,'delicious/login.html',{'error':'Invalid Credentials'})
    else:
           return render(request, 'delicious/login.html')
          
def logout(request):
    if request.method=="POST":
        if request.session['userform']:
            del request.session['userform']
    return render(request, 'delicious/login.html')

def about(request):
    return render(request,'delicious/about.html')



def founders(request):
    blogs=FoodVlogs.objects.all()
    pagination=Paginator(blogs,4)
    page = request.GET.get('page',1)
    try:
        numbers = pagination.get_page(page)
    except PageNotAnInteger:
        numbers = pagination.page(1)
    except EmptyPage:
        numbers = pagination.page(pagination.num_pages)
       
    return render(request,'delicious/blog.html',{'numbers':numbers})

def ads(request):
    ad_info=Advertisements.objects.all()
    pagination=Paginator(ad_info,3)
    page = request.GET.get('page',1)
    try:
        numbers = pagination.get_page(page)
    except PageNotAnInteger:
        numbers = pagination.page(1)
    except EmptyPage:
        numbers = pagination.page(pagination.num_pages)
       
    return render(request,'delicious/ads.html',{'numbers':numbers})

def ad_details(request,pk):
    data = Advertisements.objects.get(pk=pk)
    return render(request,'delicious/ads_detail.html',{'data':data})

def executive(request):
    executive_info = ExecutiveDetails.objects.all()
    return render(request,'delicious/executive.html',{'executive_info':executive_info})

def ex_details(request,pk):
    ex_data = ExecutiveDetails.objects.get(pk=pk)
    return render(request,'delicious/ex_details.html',{'ex_data':ex_data})



def owl(request):
    veg = Order.objects.filter(category='V')
    return render(request,'delicious/owlcarosel.html',{'img_view':veg})