# Generated by Django 5.0.7 on 2024-10-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_submit_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Std_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=200)),
                ('course_type', models.CharField(max_length=200)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
