# Generated by Django 2.2.3 on 2019-08-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multifactor', '0002_auto_20190823_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='userkey',
            name='name',
            field=models.CharField(blank=True, help_text='Easy to remember name to distinguish from any other keys of this sort you own.', max_length=30, null=True),
        ),
    ]
