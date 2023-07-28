# Generated by Django 4.2.3 on 2023-07-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Commande",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_creation", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("en instance", "en instance"),
                            ("Non livré", "Non livré"),
                            ("livré", "livré"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
            ],
        ),
    ]