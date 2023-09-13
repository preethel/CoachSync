# Generated by Django 4.2.3 on 2023-09-13 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0008_remove_enroll_paid_amount_transaction_remark_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="enroll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transactions",
                to="student.enroll",
            ),
        ),
    ]
