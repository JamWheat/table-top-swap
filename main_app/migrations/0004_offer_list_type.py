# Generated by Django 3.1.2 on 2020-10-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_wish'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='list_type',
            field=models.CharField(default='offer', max_length=50),
            preserve_default=False,
        ),
    ]