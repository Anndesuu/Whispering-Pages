# Generated by Django 5.0.1 on 2024-06-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
