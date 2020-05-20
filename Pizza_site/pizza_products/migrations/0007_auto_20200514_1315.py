# Generated by Django 3.0.3 on 2020-05-14 10:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_products', '0006_auto_20200514_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza_comment',
            name='Pizza',
        ),
        migrations.AddField(
            model_name='pizza_comment',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pizza_comment',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza_products.PizzaProduct'),
        ),
    ]
