# Generated by Django 4.2.4 on 2023-08-22 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_property_amenities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.property')),
            ],
        ),
    ]
