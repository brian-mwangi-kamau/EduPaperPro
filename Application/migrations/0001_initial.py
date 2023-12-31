# Generated by Django 4.2.6 on 2023-10-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('file', models.FileField(upload_to='files/')),
                ('level_of_education', models.CharField(choices=[('primary-school', 'Primary School'), ('high-school', 'High School'), ('tertiary', 'Tertiary Institutions')], max_length=50)),
                ('subjects', models.CharField(blank=True, choices=[('Biology', 'Biology'), ('Chemistry', 'Chemistry')], max_length=100)),
                ('courses', models.CharField(blank=True, choices=[('Architecture', 'Architecture'), ('Medicine', 'Medicine')], max_length=100)),
                ('form', models.CharField(blank=True, choices=[('Form one', 'Form One'), ('Form two', 'Form Two'), ('Form three', 'Form Three')], max_length=100)),
                ('year', models.CharField(blank=True, choices=[('First year', 'First year'), ('Second year', 'Second year'), ('Third year', 'Third year')], max_length=100)),
                ('is_free', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
