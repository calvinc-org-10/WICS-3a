# Generated by Django 4.1.1 on 2023-04-25 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("userprofiles", "0002_alter_wicsuser_user"),
        ("WICS", "0025_view_lastsap_view_materiallocationlistwithlastsap_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="countschedule",
            name="RequestFilled",
            field=models.BooleanField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="countschedule",
            name="Requestor",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="countschedule",
            name="Requestor_userid",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userprofiles.wicsuser",
            ),
        ),
    ]
