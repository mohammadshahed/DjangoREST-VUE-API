# Generated by Django 3.2.4 on 2021-06-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stripe_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]