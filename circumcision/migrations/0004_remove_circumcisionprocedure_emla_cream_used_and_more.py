# Generated by Django 4.2 on 2023-11-13 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circumcision', '0003_rename_follow_up_dates_followupvisit_visit_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circumcisionprocedure',
            name='emla_cream_used',
        ),
        migrations.RemoveField(
            model_name='circumcisionprocedure',
            name='local_anesthesia_bupivicaine',
        ),
        migrations.RemoveField(
            model_name='circumcisionprocedure',
            name='local_anesthesia_lignocaine',
        ),
        migrations.AddField(
            model_name='circumcisionprocedure',
            name='local_anesthesia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='circumcision.anesthesia'),
        ),
    ]
