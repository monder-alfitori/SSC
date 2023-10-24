# Generated by Django 4.2.5 on 2023-10-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_match_competition"),
    ]

    operations = [
        migrations.AddField(
            model_name="match",
            name="homeORaway",
            field=models.CharField(
                choices=[("home", "home"), ("away", "away")], max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="match",
            name="sGoals",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="match",
            name="sResult",
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name="match",
            name="vGoals",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="match",
            name="vResult",
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
