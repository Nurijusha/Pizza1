# Generated by Django 3.0.3 on 2020-05-14 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_products', '0005_pizza_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza_comment',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='pizza_comment',
            name='Pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='pizza_products.PizzaProduct'),
        ),
    ]
