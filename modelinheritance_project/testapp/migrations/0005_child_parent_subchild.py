# Generated by Django 2.2.2 on 2019-06-07 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20190607_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fd1', models.CharField(max_length=120)),
                ('fs2', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='child',
            fields=[
                ('parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.parent')),
                ('fd3', models.CharField(max_length=120)),
                ('fd4', models.CharField(max_length=120)),
            ],
            bases=('testapp.parent',),
        ),
        migrations.CreateModel(
            name='subchild',
            fields=[
                ('child_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.child')),
                ('fd5', models.CharField(max_length=120)),
            ],
            bases=('testapp.child',),
        ),
    ]