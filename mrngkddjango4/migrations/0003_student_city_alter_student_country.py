# Generated by Django 4.1.7 on 2023-03-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrngkddjango4', '0002_student_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default='Nairobi', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(default='Kenya', max_length=100),
        ),
    ]
