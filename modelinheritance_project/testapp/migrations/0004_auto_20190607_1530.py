# Generated by Django 2.2.2 on 2019-06-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_student1_teacher1'),
    ]

    operations = [
        migrations.CreateModel(
            name='student2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=120)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='teacher2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=120)),
                ('subject', models.CharField(max_length=100)),
                ('sal', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='teacher1',
            name='contactinfo_ptr',
        ),
        migrations.DeleteModel(
            name='student1',
        ),
        migrations.DeleteModel(
            name='teacher1',
        ),
    ]