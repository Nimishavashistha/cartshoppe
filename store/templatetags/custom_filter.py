from django import template
from store.models.customer import Customer

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "Rs."+str(number)

@register.filter(name='multiply')
def multiply(number, number1):
    return number*number1

@register.filter(name='getname')
def getname(id):
    print(id,"type= ",type(id))
    customer = Customer.objects.get(pk=id)
    return customer.first_name



    



    