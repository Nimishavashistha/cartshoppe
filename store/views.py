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
        #validation
        error_msg = None

        if(not first_name):
           error_msg = "First Name Required !!"
        elif len(first_name) < 4:
                error_msg = "First Name Must be 4 char long"
        if(not error_msg):
             phone = postData.get('phone')
             customer = Customer(first_name=first_name,
             last_name=last_name,
             phone=phone,
             email=email,
             password=password
             )
             customer.register()
        else:
            return render(request, 'signup.html',{'error': error_msg})
        

