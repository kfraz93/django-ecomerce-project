from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-input', # Apply the defined style classes
                'placeholder': 'Type your message here...' # Added a placeholder for better UX
            })
        }