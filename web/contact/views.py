from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           nombre = form.cleaned_data['name']
           correo = form.cleaned_data['email']
           mensaje = form.cleaned_data['message']

           new_message = ContactMessage(nombre=nombre, correo=correo, mensaje=mensaje )
           new_message.save()

           return redirect('success')
    else:
       form = ContactForm()
       return render(request, 'contact/contact.html', {'form': form})

def success(request):
       return render(request, 'contact/success.html')
