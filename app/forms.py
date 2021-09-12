from django import forms
from .models import Comment
from django.core.mail import EmailMessage

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {
            'text',
            'name',
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='')
    email = forms.EmailField(label='')
    text = forms.CharField(label='', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        text = self.cleaned_data['text']

        messages = EmailMessage(subject=name + 'からの問い合わせ',
                                body=text,
                                from_email=email,
                                to=["kinnkann1991@gmail.com"],
                                cc=[email])

        messages.send()