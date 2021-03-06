# Generated by Django 3.0.7 on 2020-06-09 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=11)),
                ('eductaion', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('current_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_crud.Position')),
            ],
        ),
    ]
