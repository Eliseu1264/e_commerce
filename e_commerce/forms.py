from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    nome_completo = forms.CharField(
    error_messages={'required': 'Obrigatório o preenchimento do nome'},
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )
    email     = forms.EmailField(
        error_messages={'invalid': 'Digite um email válido!'},
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    mensagem   = forms.CharField(
        error_messages={'required': 'É obrigatório o preenchimento do campo mensagem!'},
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )    
    )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com (Email errado: "+email+")")
        return email        
    
    def clean_nome_completo(self):
        nome_completo = self.cleaned_data.get("nome_completo")
        if nome_completo == None or len(nome_completo) < 5 :
            raise forms.ValidationError("O nome deve ser informado e deve ter mais de 5 caracteres!")
        return nome_completo
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Esse usuário já existe, escolha outro nome.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esse email já existe, tente outro!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("As senhas informadas devem ser iguais!")
        return data