# Generated by Django 4.1.1 on 2022-09-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0004_alter_meetings_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='participant_email',
            field=models.CharField(default='none', max_length=1000),
        ),
    ]
