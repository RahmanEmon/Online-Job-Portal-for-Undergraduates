# Generated by Django 2.2 on 2020-02-07 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_boy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Your Name', max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('phone', models.CharField(default='01715254640', max_length=500)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('job', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
            ],
        ),
    ]
