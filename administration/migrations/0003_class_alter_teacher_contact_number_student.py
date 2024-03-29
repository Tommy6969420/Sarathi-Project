# Generated by Django 4.1.13 on 2024-02-15 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administration", "0002_teacher_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
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
                ("name", models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name="teacher",
            name="contact_number",
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=64)),
                ("date_of_birth", models.DateField()),
                ("parents_name", models.CharField(max_length=64)),
                ("address", models.CharField(max_length=64)),
                ("contact", models.CharField(max_length=10)),
                (
                    "for_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administration.class",
                    ),
                ),
            ],
        ),
    ]
