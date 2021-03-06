# Generated by Django 4.0.4 on 2022-05-25 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0004_cartitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.customer')),
            ],
        ),
    ]
