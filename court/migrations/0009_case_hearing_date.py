# Generated by Django 3.1.7 on 2021-04-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0008_case_verdict'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='hearing_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]