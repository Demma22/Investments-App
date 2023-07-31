# Generated by Django 4.2.3 on 2023-07-28 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("uap", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Investment",
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
                ("deposit", models.DecimalField(decimal_places=2, max_digits=10)),
                ("interest", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="runninginvestments",
            name="plus_interest",
        ),
        migrations.DeleteModel(
            name="EarnedInterest",
        ),
        migrations.DeleteModel(
            name="RunningInvestments",
        ),
        migrations.DeleteModel(
            name="TotalDeposit",
        ),
    ]
