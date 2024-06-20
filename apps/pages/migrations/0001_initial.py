# Generated by Django 4.2.5 on 2024-05-17 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_statement', models.TextField(verbose_name='little sign mission statement')),
                ('vision_statement', models.TextField(verbose_name='little sign vision statement')),
            ],
            options={
                'verbose_name': 'AboutUs',
                'verbose_name_plural': 'AboutUs',
            },
        ),
        migrations.CreateModel(
            name='OrganisationMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Full name')),
                ('position', models.CharField(max_length=50, verbose_name='Position in company')),
                ('linked_in', models.URLField(null=True, verbose_name='LinkedIn profile link')),
                ('twitter', models.URLField(null=True, verbose_name='Twitter profile link')),
                ('facebook', models.URLField(null=True, verbose_name='Facebook profile link')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
