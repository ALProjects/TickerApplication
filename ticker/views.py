from django.shortcuts import render, redirect
from .models import TickerModel
from .forms import SubscribeForm
from django.core.mail import send_mail
from django.conf import settings

import yfinance as yf


# Create your views here.

def delete_sub(request, sub_id):
    subscription = TickerModel.objects.get(pk=sub_id)
    subscription.delete()
    return redirect('/home')


def send_update(request, sub_id):
    subscription = TickerModel.objects.get(pk=sub_id)
    recipient = subscription.subscriber_email
    subject = "Your ticker update"
    message = 'Your ticker: {} \nTicker Price: {} \n'.format(subscription.ticker.upper(), subscription.ticker_price)

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient])
    return redirect('/home')


def index(request):
    subscription_array = []

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['desired_ticker']
            email = form.cleaned_data['subscriber_email']
            fetched_ticker = yf.Ticker(ticker.upper())
            ticker_price = (fetched_ticker.info['regularMarketPrice'])
            if TickerModel.objects.filter(subscriber_email=email, ticker=ticker.upper()):
                # This ticker already exists
                print("Ticker already exists")
            else:
                ticker_info = TickerModel()
                ticker_info.subscriber_email = email
                ticker_info.ticker = ticker.upper()
                ticker_info.ticker_price = ticker_price
                ticker_info.save()
                form = SubscribeForm()
    else:
        form = SubscribeForm()

    for ticker in TickerModel.objects.all():
        subscription_array.append(ticker)

    context = {
        'form': form,
        'subscriptions': subscription_array
    }
    return render(request, 'index.html', context)
