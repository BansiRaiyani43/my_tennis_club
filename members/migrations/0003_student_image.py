# Generated by Django 5.2.2 on 2025-07-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_student_age_student_email_student_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
