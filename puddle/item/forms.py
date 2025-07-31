from django import forms
from  .models import Item

WIDGET_STYLE_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': WIDGET_STYLE_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': WIDGET_STYLE_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': WIDGET_STYLE_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': WIDGET_STYLE_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': WIDGET_STYLE_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': WIDGET_STYLE_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': WIDGET_STYLE_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': WIDGET_STYLE_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': WIDGET_STYLE_CLASSES
            })
        }