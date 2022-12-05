# Generated by Django 4.1.3 on 2022-12-05 08:09

from django.db import migrations, models
import django.db.models.deletion
import todo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                ("image", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=50)),
                ("details", models.CharField(max_length=300)),
                ("has_been_done", models.BooleanField(blank=True, default=False)),
                ("date_creation", models.DateField(auto_now_add=True)),
                ("date_completion", models.DateField(blank=True, null=True)),
                (
                    "deadline_date",
                    models.DateField(validators=[todo.models.validate_date]),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="todo.category",
                    ),
                ),
            ],
        ),
    ]