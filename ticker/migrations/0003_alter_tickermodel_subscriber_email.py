# Generated by Django 3.2.9 on 2021-11-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0002_alter_tickermodel_ticker_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickermodel',
            name='subscriber_email',
            field=models.EmailField(max_length=254),
        ),
    ]
