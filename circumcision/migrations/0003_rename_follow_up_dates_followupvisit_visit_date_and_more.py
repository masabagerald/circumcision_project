# Generated by Django 4.2 on 2023-11-12 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circumcision', '0002_anesthesia_circumcisionprocedure_end_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followupvisit',
            old_name='follow_up_dates',
            new_name='visit_date',
        ),
        migrations.RemoveField(
            model_name='followupvisit',
            name='circumcision_procedure',
        ),
        migrations.AddField(
            model_name='followupvisit',
            name='Client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='circumcision.client'),
        ),
        migrations.AddField(
            model_name='followupvisit',
            name='attending_health_worker',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
