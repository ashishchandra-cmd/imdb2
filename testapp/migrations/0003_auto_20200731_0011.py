# Generated by Django 3.0.4 on 2020-07-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200730_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Summary',
            field=models.TextField(),
        ),
    ]
