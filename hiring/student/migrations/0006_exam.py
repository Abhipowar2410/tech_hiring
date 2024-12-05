# Generated by Django 5.0.7 on 2024-07-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_certificate_file_alter_student_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('optionA', models.CharField(max_length=50)),
                ('optionB', models.CharField(max_length=50)),
                ('optionC', models.CharField(max_length=50)),
                ('optionD', models.CharField(max_length=50)),
                ('correct_ans', models.CharField(max_length=50)),
            ],
        ),
    ]
