# Generated by Django 4.2.4 on 2023-08-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_student_access_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="canvas_lms_id",
            field=models.CharField(default=111, unique=True),
            preserve_default=False,
        ),
    ]
