# Generated by Django 3.2.4 on 2021-07-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210703_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='carrossel1',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/projeto/thumb'),
        ),
        migrations.AddField(
            model_name='post',
            name='carrossel2',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/projeto/thumb'),
        ),
    ]
