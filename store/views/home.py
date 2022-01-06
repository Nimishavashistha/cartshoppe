from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.views import View
# print(make_password('1234'))

class Index(View):
    def get(self, request):
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
        print(request.session.get('email'))
        return render(request, 'index.html', data)
    
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('homepage')
        
           
