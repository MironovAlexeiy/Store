from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'youemail@example.ru'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Минск, ул. Мира, д. 11, кв. 11'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')

    def save(self, commit=True):
        self.instance.update_after_payment()
        return super(OrderForm, self).save(commit=True)
