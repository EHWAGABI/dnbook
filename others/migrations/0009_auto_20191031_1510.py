# Generated by Django 2.2.6 on 2019-10-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0008_auto_20191010_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='picture',
            field=models.ImageField(blank=True, upload_to='Culture/', verbose_name='이미지 등록'),
        ),
    ]
