# Generated by Django 3.0.3 on 2020-02-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200209_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default='General', max_length=50),
        ),
    ]
