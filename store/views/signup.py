from django.shortcuts import redirect, render
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
     def get(self, request):
          return render(request, 'signup.html')
      
     def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')

        customer = Customer(first_name=first_name,
                                 last_name=last_name,
                                 phone=phone,
                                 email=email,
                                 password=password
                                )
        #validation
        error_msg = None
        value = {
            'first_name':first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_msg = self.validateCustomer(customer)
        if(not error_msg):
            #  print(first_name,last_name,phone,email,password)
             customer.password = make_password(customer.password)
             customer.register()
             return redirect('homepage')
        else:
            data = {
                'error': error_msg, 
                'values':value
            }
            return render(request, 'signup.html',data)
        
     def validateCustomer(self, customer):
        error_msg = None
        if(not customer.first_name):
           error_msg = "First Name Required !!"
        elif len(customer.first_name) < 4:
                error_msg = "First Name Must be 4 char long"
        elif not customer.last_name:
            error_msg = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_msg = "Last Name must be 4 char long or more"
        elif not customer.phone:
            error_msg = "Phone number Required"
        elif len(customer.phone)<10:
            error_msg = "Phone Number must be 10 char long"
        elif len(customer.password) < 6:
            error_msg = "Password must be 6 char long"
        elif len(customer.email)<5:
            error_msg = "Email must be 5 char long"
        elif customer.isExists():
            error_msg = "Email address already registered..."
        return error_msg



      

    
