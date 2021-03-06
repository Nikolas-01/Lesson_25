# Generated by Django 3.0.5 on 2020-05-20 23:19

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0012_infofile'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='poet',
            managers=[
                ('poets', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='poet',
            name='last_name',
            field=models.CharField(db_index=True, default='n/a', max_length=100),
        ),
        migrations.DeleteModel(
            name='InfoFile',
        ),
    ]
