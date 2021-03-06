# Generated by Django 2.1.2 on 2019-10-23 12:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_Number', models.IntegerField(default=0)),
                ('office_Title', models.CharField(max_length=50)),
                ('complaint', models.CharField(max_length=100)),
                ('additional_Info', models.TextField(default='unkown', max_length=50)),
                ('solution', models.CharField(max_length=100)),
                ('occurance', models.IntegerField(default=0)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
