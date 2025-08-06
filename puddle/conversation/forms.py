from django import forms

from .models import ConversationMessage

# Define a common style for text areas or text inputs in your forms,
# including dark mode classes for background, border, and text color.
MESSAGE_INPUT_STYLE_CLASSES = 'w-full py-4 px-6 rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-blue-500 focus:border-blue-500 transition-colors duration-300'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': MESSAGE_INPUT_STYLE_CLASSES, # Apply the defined style classes
                'placeholder': 'Type your message here...' # Added a placeholder for better UX
            })
        }