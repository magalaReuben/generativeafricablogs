# Generated by Django 5.1.4 on 2025-01-20 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='section_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='subsection',
            name='sub_section_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
