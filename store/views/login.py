from django.shortcuts import redirect, render, HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_msg = 'Email or password invalid !!'
        else:
            error_msg = 'Email or password invalid !!'
        return render(request, 'login.html', {'error': error_msg})
    

def logout(request):
    request.session.clear()
    return redirect('login')

class PasswordResetView(View):
    def get(self,request):
         return render(request, 'password_reset.html')
     
class PasswordResetDoneView(View):
    def get(self,request):
         return render(request, 'password_reset_done.html')
     
class PasswordResetConfirmView(View):
    def get(self,request):
         return render(request, 'password_reset_confirm.html')
     
class PasswordResetCompleteView(View):
    def get(self,request):
         return render(request, 'password_reset_complete.html')




