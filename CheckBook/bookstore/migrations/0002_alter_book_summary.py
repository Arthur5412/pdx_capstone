# Generated by Django 3.2.8 on 2022-01-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Summary',
            field=models.CharField(max_length=120, null=True),
        ),
    ]