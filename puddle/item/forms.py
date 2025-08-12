from django import forms
from .models import Item

# The WIDGET_STYLE_CLASSES constant is no longer needed since we have a reusable
# component class defined in input.css. We can now use 'form-input' directly.

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            # We are now using our 'form-input' component class
            'category': forms.Select(attrs={
                'class': 'form-input'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-input'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            # We are now using our 'form-input' component class
            'name': forms.TextInput(attrs={
                'class': 'form-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-input'
            }),
            # The checkbox requires different styling, but we can make it
            # consistent with the new theme colors.
            'is_sold': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }
