from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from store.models import customer

# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.get_all_products_by_categoryid(categoryId)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')
        #validation
        error_msg = None
        value = {
            'first_name':first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        if(not first_name):
           error_msg = "First Name Required !!"
        elif len(first_name) < 4:
                error_msg = "First Name Must be 4 char long"
        elif not last_name:
            error_msg = "Last Name Required"
        elif len(last_name) < 4:
            error_msg = "Last Name must be 4 char long or more"
        elif not phone:
            error_msg = "Phone number Required"
        elif len(phone)<10:
            error_msg = "Phone Number must be 10 char long"
        elif len(password) < 6:
            error_msg = "Password must be 6 char long"
        elif len(email)<5:
            error_msg = "Email must be 5 char long"
        
        if(not error_msg):
             customer = Customer(first_name=first_name,
             last_name=last_name,
             phone=phone,
             email=email,
             password=password
             )
             customer.register()
             return render(request, 'index.html')
        else:
            data = {
                'error': error_msg, 
                'values':value
            }
            return render(request, 'signup.html',data)
        

