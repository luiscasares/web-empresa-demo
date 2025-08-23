from django import forms

class ContactForm(forms.Form):
    """Clase para definir el formulario de contacto General"""
    name = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Escribe tu nombre', 'class':'form-control'}))
    email = forms.EmailField(label="Email", min_length=3, max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Escribe tu email', 'class':'form-control'}))
    mensaje = forms.CharField(label="Mensaje", min_length=10,max_length=1000, required=True, widget=forms.Textarea(attrs={'placeholder':'Escribe tu mensaje', 'rows':3,'class':'form-control'}))
