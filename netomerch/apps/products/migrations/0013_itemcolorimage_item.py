# Generated by Django 3.2.8 on 2021-12-11 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_refactor_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcolorimage',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='products.item'),
        ),
    ]
