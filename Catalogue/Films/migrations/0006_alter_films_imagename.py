# Generated by Django 4.2.5 on 2023-10-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0005_alter_films_imagename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='imageName',
            field=models.FileField(upload_to='./static/images/'),
        ),
    ]
