# Generated by Django 3.0.6 on 2020-06-06 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0021_auto_20200529_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_line_signal', models.CharField(blank=True, max_length=200, null=True)),
                ('poem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='poems.Poem')),
            ],
        ),
    ]
