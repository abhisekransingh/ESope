from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.products import Product
from .models.category import Category
from .models.custome import Customes
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from django.db.models import Avg,Min,Max,Count,Aggregate
from django.db.models import Avg,Min,Max,Count,Aggregate
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

# Create your views here.

#Message handlings
error_message=None






'''
we are stating our code
'''
def index(request):
    product=None
    category=Category.get_all_category()
    print(product)
    getCatID=request.GET.get("category")
    if(getCatID):
        product=Product.get_producr_ByCategoryID(getCatID)
    else:
        product=Product.get_product()

    data={}
    data['category']=category   
    data['product']=product
    print('email',request.session.get('email'))
    
    print('costemr',request.session.get('coustomer_id'))
    getemail=request.session.get('email')
    if(getemail!=None):
        get_username=Customes.loggedin_email(getemail)
        data['name']=get_username.first_name
    return render(request,'index.html',data)

def validate_data(createCustomer):
    global error_message
    if (not createCustomer.first_name):
        print('ABCD')
        error_message="First Name Required"
        
    elif(len(createCustomer.first_name)<4):
        error_message="First Name mor that 4 charector"
    elif(not createCustomer.last_name):
        error_message="Last Name Required"
    elif(not createCustomer.number):
        error_message="Number Required"
    elif(not createCustomer.password):
        error_message="Password must be required"
    elif createCustomer.isexit():
        error_message="Email already Exits"
    return error_message
def validate_login(logincheck):
    print(53,'login')
    global error_message
    if(not logincheck.email ):
        error_message="Username should not empty"
        return error_message
    elif(not logincheck.password ):
        error_message="Password should not empty"
        return error_message
    
def signUp(request):
    
    if request.method=="GET":
        return render(request,'SignUp&Login/signUp.html')
    else:
        postdata=request.POST
        first_name=postdata.get('firstname')
        last_name=postdata.get('lastname')
        email=postdata.get('email')
        number=postdata.get('number')
        password=postdata.get('password')
        print(first_name,'***********')
        createCustomer=Customes(first_name=first_name,last_name=last_name,email=email,number=number,password=password)
        error_message=validate_data(createCustomer)
  
        if not error_message:
            
            createCustomer.password=make_password(createCustomer.password)
            createCustomer.registor()
            return redirect("homepage")
        else:
            return render(request,'SignUp&Login/signUp.html',{'error':error_message})
        
def login(request):
  
    global error_message
    if request.method=="GET":
        return render(request,'SignUp&Login/LogIn/LogIn.html')
    else:
        # import pdb
        # pdb.set_trace()
        
        login_data=request.POST
        email=login_data.get('email')
        print(email)
        password=login_data.get('password')
        print(password)
        logincheck=Customes(email=email,password=password)
        error_message=validate_login(logincheck)
        print('lucky')
        print(error_message)
        
        if not error_message:
            
            getcustomer_email=Customes.loggedin_email(email)
            password=check_password(password,getcustomer_email.password)
            if getcustomer_email and password:
                request.session['coustomer_id']=getcustomer_email.id
                request.session['email']=getcustomer_email.email
                return redirect("homepage")
            elif(not getcustomer_email or not password):

                error_message="Invalid Email or Password!!"
            else:
                error_message="Invalid Email or Password!!"
                return render(request,'SignUp&Login/LogIn/LogIn.html',{'error':error_message})
        
        return render(request,'SignUp&Login/LogIn/LogIn.html',{'error':error_message})


@receiver(pre_save,sender=Customes)
def save_data(sender,instance,**kwargs):
    print('run second')

    



            
