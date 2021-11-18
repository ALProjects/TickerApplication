from django import forms


class SubscribeForm(forms.Form):
    subscriber_email = forms.EmailField(label="Your Email", max_length=100)
    desired_ticker = forms.CharField(label="Your Ticker", max_length=5)
