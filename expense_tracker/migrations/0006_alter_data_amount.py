# Generated by Django 4.1.4 on 2023-01-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0005_alter_data_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
