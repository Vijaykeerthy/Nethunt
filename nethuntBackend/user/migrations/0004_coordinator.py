# Generated by Django 4.1.4 on 2023-01-10 09:51

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_user_id_alter_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coordinator",
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
                ("coordinatorName", models.CharField(max_length=20)),
                ("coordinatorEmail", models.EmailField(max_length=254)),
                (
                    "coordinatorPhone",
                    models.CharField(
                        max_length=10, validators=[user.models.validPhone]
                    ),
                ),
                ("CoordinatorPhoto", models.FileField(upload_to="image/coordinator")),
            ],
        ),
    ]
