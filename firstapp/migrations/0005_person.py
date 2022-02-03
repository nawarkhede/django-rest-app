# Generated by Django 3.1.14 on 2022-02-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0004_city"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=30)),
            ],
        ),
    ]