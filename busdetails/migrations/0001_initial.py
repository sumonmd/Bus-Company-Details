# Generated by Django 2.2.3 on 2019-07-07 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('head_office', models.TextField()),
                ('staff_count', models.IntegerField(default=0)),
            ],
        ),
    ]
