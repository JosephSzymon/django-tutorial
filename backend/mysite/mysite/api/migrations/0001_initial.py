# Generated by Django 3.2.7 on 2021-09-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('caliber', models.CharField(max_length=10)),
            ],
        ),
    ]