# Generated by Django 2.2.10 on 2021-07-26 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210726_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
    ]
