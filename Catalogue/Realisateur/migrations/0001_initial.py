# Generated by Django 4.2.5 on 2023-10-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=250)),
                ('nom', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
