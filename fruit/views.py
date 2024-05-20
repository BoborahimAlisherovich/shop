from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm
from .bot import send_message
from .models import Contact,Product
from django.views.generic import View,CreateView

def home_view(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, "index.html" ,context=context)

def shop_view(request):
    return render(request,"shop.html")

class ContactView(View):
    template_name = "contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        contact = Contact(first_name=name,email=email,description=message)
        contact.save()
        
        send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

        return HttpResponseRedirect(reverse('home-page'))   

# class ContactView(CreateView):
#     model = Contact
#     form_class = ContactForm
#     template_name = "contact.html"
#     success_url ='/'


# def contact_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('first_name', '')
#         email = request.POST.get('email', '')
#         message = request.POST.get('description', '')
#         contact = Contact(first_name=name,email=email,description=message)
#         contact.save()
        
#         send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

#         return render(request, 'contact.html')
        
#     else:
#         return render(request, "contact.html")