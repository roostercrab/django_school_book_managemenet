# Generated by Django 2.1.5 on 2019-02-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_book', '0004_student_total_no_of_pages_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_publication',
            field=models.DateField(null=True),
        ),
    ]
