from django.shortcuts import render,redirect
from .forms import ContactInfoForm
from django.views import View
from django.contrib import messages
from .models import Address_Info 

class ContactInfoView(View):
    def get(self, request):
        address_info = Address_Info.objects.all()
        form = ContactInfoForm()
        return render(request, 'myapp/contact.html', {'form': form,'address_infos': address_info })

    def post(self, request):
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Submitted Successfully')
            form.save()
            return redirect('contact')
        return render(request, 'myapp/contact.html', {'form': form})

   



