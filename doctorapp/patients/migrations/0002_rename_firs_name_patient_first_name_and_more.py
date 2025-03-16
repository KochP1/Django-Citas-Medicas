# Generated by Django 5.1.7 on 2025-03-16 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='firs_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_record', to='patients.patient'),
        ),
    ]
