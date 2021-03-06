# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='Slug')),
                ('submit_name', models.CharField(max_length=128, verbose_name='Submit bottom name')),
                ('success_message', models.TextField(blank=True, verbose_name='Success message')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Form config',
                'verbose_name_plural': 'Forms configs',
            },
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Label')),
                ('help_text', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Help text')),
                ('name', models.SlugField(max_length=100, verbose_name='Name')),
                ('field_type', models.IntegerField(choices=[(1, 'Single line text'), (2, 'Multi line text'), (3, 'Email'), (13, 'Number'), (14, 'URL'), (4, 'Check box'), (5, 'Check boxes'), (6, 'Drop down'), (7, 'Multi select'), (8, 'Radio buttons'), (9, 'File upload'), (10, 'Date'), (11, 'Date/time'), (15, 'Date of birth'), (12, 'Hidden')], verbose_name='Type')),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('choices', models.TextField(blank=True, null=True, verbose_name='Choices')),
                ('default', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Default')),
                ('placeholder', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Placeholder')),
                ('order', models.IntegerField(default=500, verbose_name='Sort ordering')),
                ('form_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='contacts.FormConfig', verbose_name='Form Config')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='FormLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('referrer', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Referrer')),
                ('data', models.TextField(blank=True, null=True, verbose_name='Data')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('form_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.FormConfig', verbose_name='Form Config')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Form log',
                'verbose_name_plural': 'Form logs',
            },
        ),
        migrations.CreateModel(
            name='OfficeFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('key', models.SlugField(max_length=128, verbose_name='Key')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Value')),
            ],
            options={
                'ordering': ['office', 'name'],
                'verbose_name': 'Office feature',
                'verbose_name_plural': 'Office features',
            },
        ),
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
        migrations.AlterField(
            model_name='office',
            name='center_latitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=19, null=True, verbose_name='Center latitude'),
        ),
        migrations.AlterField(
            model_name='office',
            name='center_longitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=19, null=True, verbose_name='Center longitude'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='officefeature',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='contacts.Office', verbose_name='Office'),
        ),
    ]
