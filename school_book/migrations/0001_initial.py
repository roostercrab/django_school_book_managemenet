# Generated by Django 2.1.5 on 2019-02-12 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=256)),
                ('date_of_publication', models.DateField()),
                ('no_of_pages', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=300)),
                ('school_email_id', models.EmailField(max_length=254)),
                ('principal_name', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=10)),
                ('school_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('student_email_id', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=6)),
                ('books', models.ManyToManyField(to='school_book.Book')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_book.School')),
            ],
        ),
    ]