# Generated by Django 2.1.7 on 2019-03-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginSignup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addsignup',
            name='Potentia',
            field=models.IntegerField(default=0),
        ),
    ]
