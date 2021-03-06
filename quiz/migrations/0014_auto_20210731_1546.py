# Generated by Django 3.2.5 on 2021-07-31 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_listeningtest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresult',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.telegramuser'),
        ),
    ]
