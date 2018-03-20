from django import forms
from .models import SellItem

class SellItemForm(forms.ModelForm):
    
    class Meta:
        model = SellItem
        fields = ('title', 'content', 'price', 'max_buy', 'image')
        