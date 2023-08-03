# Generated by Django 4.2.3 on 2023-07-29 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_options_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(default="01718925923", max_length=11, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A", "Admin"),
                    ("AS", "Admin Staff"),
                    ("OA", "Organization Admin"),
                    ("OS", "Organization Staff"),
                    ("S", "student"),
                    ("T", "teacher"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]
