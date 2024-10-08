# Generated by Django 4.2.13 on 2024-08-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0040_orderitem_fix_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("preparing", "Preparing"),
                    ("delivering", "Delivering"),
                    ("done", "Done"),
                    ("canceled", "Canceled"),
                ],
                db_index=True,
                default="new",
                max_length=255,
            ),
        ),
    ]
