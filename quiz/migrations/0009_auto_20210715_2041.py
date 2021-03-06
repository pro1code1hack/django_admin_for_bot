# Generated by Django 3.2.5 on 2021-07-15 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_userresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'subcriptions',
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.subscription'),
        ),
    ]
