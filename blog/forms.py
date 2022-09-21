from django import forms
from .models import FeedBack

class FeedBackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'contact-form-input w-input', 'placeholder': ''})
        self.fields['phone'].widget.attrs.update({'class': 'contact-form-input w-input', 'placeholder': ''})
        self.fields['text'].widget.attrs.update({'class': 'contact-form-input w-input', 'placeholder': ''})

    class Meta:
        model = FeedBack
        fields = ('name', 'phone', 'text')