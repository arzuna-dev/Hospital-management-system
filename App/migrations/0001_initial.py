# Generated by Django 3.2.13 on 2022-07-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
