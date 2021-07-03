# Generated by Django 3.2.4 on 2021-07-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/projeto/thumb'),
        ),
    ]
