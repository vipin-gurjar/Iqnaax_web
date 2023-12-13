from django.shortcuts import render,redirect
from django.views import View
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from .models import Customer
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class CustomerRegistrationView(View):
    def get(self, request):
       form = CustomerRegistrationForm()
       return render(request, 'myapp/customerregistration.html',{'form':form})
    
    def post(self, request):
       form= CustomerRegistrationForm(request.POST)
       if form.is_valid():
          messages.success(request, 'Congratulations!! You Registered  Successfully')
          form.save()
          return redirect('registration')
       return render(request, 'myapp/customerregistration.html',{'form':form})
    
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
       form = CustomerProfileForm()
       return render(request, 'myapp/profile.html', {'form':form, 'active':'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=usr, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, 'Conguratioulations!! Profile Upadated Successfully')
            return redirect('profile')
        return render(request, 'myapp/profile.html', {'form':form, 'active':'btn-primary'})
     
    
# @login_required
def address(request):
   add = Customer.objects.filter(user=request.user)
   return render(request, 'myapp/address.html', {'add':add, 'active':'btn-primary'})
   






























        

