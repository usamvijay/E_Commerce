# Generated by Django 3.2.5 on 2021-07-29 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_catagories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Catagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Catagory_name', models.CharField(max_length=20)),
                ('Cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display', to='Myapp.catagories')),
            ],
        ),
    ]
