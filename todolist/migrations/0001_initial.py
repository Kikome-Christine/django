# Generated by Django 4.2 on 2023-05-21 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateField(default='2023-05-21')),
                ('due_date', models.DateField(default='2023-05-21')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todolist.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
