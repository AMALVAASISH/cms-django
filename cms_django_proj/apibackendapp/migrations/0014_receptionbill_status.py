# Generated by Django 4.2.7 on 2023-11-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibackendapp', '0013_receptionbill_token_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='receptionbill',
            name='status',
            field=models.CharField(choices=[('paid', 'paid')], default='paid', max_length=4),
        ),
    ]
