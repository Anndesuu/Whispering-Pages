# Generated by Django 5.0.1 on 2024-06-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_newrecipe_recipeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
