# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuiduser.fields
import re
import django.utils.timezone
import django.core.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('username', uuiduser.fields.NullCharField(blank=True, max_length=255, unique=True, null=True, validators=[django.core.validators.RegexValidator(re.compile(b"([a-zA-Z][a-zA-Z0-9])|([a-zA-Z](?![-_'.]{2})[\\w.'-]+[a-zA-Z0-9])"), code=b'invalid')])),
                ('name', models.CharField(default=b'', max_length=255)),
                ('short_name', models.CharField(default=b'', max_length=255)),
                ('is_staff', models.BooleanField(default=False, help_text=b'Can log in to admin.')),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
