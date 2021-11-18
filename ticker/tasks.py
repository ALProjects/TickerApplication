from .models import TickerModel
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

import yfinance as yf


@shared_task
def update_tickers_and_email():
    #go through each ticker and update their ticker prices
    ticker_subscriber_dict = {}

    #Make a dictionary mapping all the current tickers and subscribers
    for ticker_model in TickerModel.objects.all():
        if ticker_model.subscriber_email in ticker_subscriber_dict:
            ticker_subscriber_dict[ticker_model.subscriber_email].append(ticker_model)
        else:
            ticker_subscriber_dict[ticker_model.subscriber_email] = [ticker_model]

    #Email that subscriber
    #continue with next sub
    for key in ticker_subscriber_dict:
        message = "Your subscriptions\n"
        list_of_tickers = ticker_subscriber_dict[key]
        for ticker in list_of_tickers:
            message += 'Ticker: {} Current Price: {}\n'.format(ticker.ticker.upper(), ticker.ticker_price)
            message += '================================\n'
        subject = "Your scheduled ticker update"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [key])


@shared_task
def update_prices():
    ticker_set = set()
    # Update the ticker prices
    for ticker in ticker_set:
        fetched_ticker = yf.Ticker(ticker.upper())
        updated_ticker_price = (fetched_ticker.info['regularMarketPrice'])
        TickerModel.objects.filter(ticker=ticker).update(ticker_price=updated_ticker_price)