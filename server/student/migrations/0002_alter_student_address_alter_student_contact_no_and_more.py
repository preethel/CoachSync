# Generated by Django 4.2.3 on 2023-07-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="address",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="contact_no",
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="date_of_birth",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="emergency_contact_no",
            field=models.CharField(max_length=11, null=True),
        ),
    ]
