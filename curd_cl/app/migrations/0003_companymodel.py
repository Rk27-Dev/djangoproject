# Generated by Django 2.2.2 on 2019-06-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190606_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='companymodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=50)),
                ('ceo', models.CharField(max_length=20)),
            ],
        ),
    ]
