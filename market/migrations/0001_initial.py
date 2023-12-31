# Generated by Django 4.2.6 on 2023-10-22 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TopOfTheBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_bid_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('best_bid_size', models.PositiveIntegerField()),
                ('best_offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('best_offer_size', models.PositiveIntegerField()),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.symbol')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('side', models.CharField(max_length=4)),
                ('quantity', models.PositiveIntegerField()),
                ('order_id', models.CharField(max_length=255)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.symbol')),
            ],
        ),
    ]
