from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    email = forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'placeholder': 'Correo'})
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'placeholder': 'Mensaje'})
    )