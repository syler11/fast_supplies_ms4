# Generated by Django 3.2 on 2022-04-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
