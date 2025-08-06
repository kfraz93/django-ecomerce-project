from django import forms
from  .models import Item

# UPDATED WIDGET_STYLE_CLASSES to include dark mode styling and transitions
WIDGET_STYLE_CLASSES = 'w-full py-4 px-6 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-blue-500 focus:border-blue-500 transition-colors duration-300'

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
            }),
            'is_sold': forms.CheckboxInput(attrs={ # Checkbox styling for dark mode
                'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600 transition-colors duration-300'
            }),
        }