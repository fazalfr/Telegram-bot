# Generated by Django 4.1.2 on 2023-02-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('stupid', 'Stupid'), ('fat', 'Fat'), ('dumb', 'Dumb')], max_length=10, unique=True)),
                ('call_count', models.IntegerField(default=0)),
            ],
        ),
    ]
