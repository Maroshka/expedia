# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_auto_20171229_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='lengthOfStay',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='maxGuestRating',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], null=True, max_digits=2, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='maxStarRating',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], null=True, max_digits=2, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='maxTotalRate',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], null=True, max_digits=2, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='minGuestRating',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], null=True, max_digits=2, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='minStarRating',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], null=True, max_digits=2, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='minTotalRate',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0.0)], null=True, max_digits=2, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='deals',
            name='regionIds',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
