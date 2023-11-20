# Generated by Django 4.2 on 2023-11-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circumcision', '0008_alter_client_payment_method_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalhistory',
            old_name='client_concented',
            new_name='eligibility_after_examination',
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='client_consented',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='consent_form',
            field=models.FileField(null=True, upload_to='concent_forms/'),
        ),
    ]
