# Generated by Django 4.2.3 on 2023-07-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_remove_recipe_difficulty_recipe_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe", name="description", field=models.TextField(),
        ),
    ]
