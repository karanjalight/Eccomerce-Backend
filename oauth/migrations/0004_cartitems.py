# Generated by Django 4.0.4 on 2022-05-25 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0003_alter_product_category_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.product')),
            ],
        ),
    ]
