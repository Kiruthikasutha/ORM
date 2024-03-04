# Generated by Django 5.0.2 on 2024-02-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_DB',
            fields=[
                ('book_name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('published_year', models.IntegerField()),
                ('bookno', models.IntegerField(primary_key='bookno', serialize=False)),
                ('bookrate', models.IntegerField()),
            ],
        ),
    ]
