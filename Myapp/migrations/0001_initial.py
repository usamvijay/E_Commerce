# Generated by Django 3.2.5 on 2021-07-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('contact', models.CharField(max_length=15)),
                ('State', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('Cpassword', models.CharField(max_length=20)),
            ],
        ),
    ]
