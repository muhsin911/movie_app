# Generated by Django 4.2 on 2023-04-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="Image",
            field=models.ImageField(default="mdmzx", upload_to="gallery"),
            preserve_default=False,
        ),
    ]
