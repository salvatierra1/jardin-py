# Generated by Django 4.2.5 on 2023-09-13 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido/s')),
            ],
            options={
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]
