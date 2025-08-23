from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from webempresa.settings import EMAIL_HOST_USER
from .forms import ContactForm
# Create your views here.

def contact(request):
    """Vista para contacto"""
    # print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('mensaje', '')
            email_message = EmailMessage(
                "Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                EMAIL_HOST_USER,
                ["luis.casares.gomeztagle@gmail.com"],
                reply_to=[email]
            )
            try:
                email_message.send()
                # Redireccion a OK
                return redirect(reverse('contact')+"?ok")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect(reverse('contact')+"?fail")

    return render (request, 'contact/contact.html', {'form':contact_form})
