# Generated by Django 2.2.6 on 2019-11-07 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmap', '0021_auto_20191104_0117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookstore',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='bookstore',
            name='saup',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='000-00-00000 형식에 맞게 입력해주세요.', regex='^\\d{3}\\-\\d{2}\\-\\d{5}$')]),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='000-0000-0000과 같은 형식으로 입력해주세요.', regex='^\\d{2,3}\\-\\d{3,4}\\-\\d{4}$')]),
        ),
    ]
