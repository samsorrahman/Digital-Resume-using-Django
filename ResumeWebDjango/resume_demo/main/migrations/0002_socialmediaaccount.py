# Generated by Django 4.1.4 on 2023-04-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Twitter', 'Twitter'), ('LinkedIn', 'LinkedIn')], max_length=10)),
                ('username', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
