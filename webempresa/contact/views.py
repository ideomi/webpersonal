from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContacForm
# Create your views here.

def contact(request):
    contact_form = ContacForm()
    if request.method == 'POST':
        contact_form = ContacForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            return redirect(reverse('contact')+'?ok')


    return render(request,'contact/contact.html',{'form':contact_form})

