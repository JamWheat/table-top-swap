# Generated by Django 3.1.2 on 2020-10-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_offer_list_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='list_type',
            field=models.CharField(choices=[('1', 'New'), ('2', 'Like New'), ('3', 'Good'), ('4', 'Fair'), ('5', 'Poor')], max_length=1),
        ),
    ]
