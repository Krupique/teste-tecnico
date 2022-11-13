# Generated by Django 4.1.3 on 2022-11-13 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portal_noticias", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comentario",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "noticia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portal_noticias.noticia",
                    ),
                ),
            ],
        ),
    ]
