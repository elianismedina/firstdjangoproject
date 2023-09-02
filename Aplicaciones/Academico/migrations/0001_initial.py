# Generated by Django 4.2.4 on 2023-09-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "codigo",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("creditos", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
