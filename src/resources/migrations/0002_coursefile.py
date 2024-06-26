# Generated by Django 5.0.4 on 2024-05-31 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseFile",
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
                ("title", models.CharField(max_length=255)),
                ("link", models.TextField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resources.course",
                    ),
                ),
            ],
        ),
    ]
