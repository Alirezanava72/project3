# Generated by Django 4.2.4 on 2023-08-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_renting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='renting',
            options={'ordering': ['-available_date']},
        ),
        migrations.AlterField(
            model_name='renting',
            name='available_date',
            field=models.DateField(verbose_name='availability Date'),
        ),
    ]
