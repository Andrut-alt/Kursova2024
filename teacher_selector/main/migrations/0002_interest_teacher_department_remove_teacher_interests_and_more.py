# Generated by Django 5.1.2 on 2024-11-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.CharField(choices=[('system_desygn', 'Cистемного проектування'), ('radio_physic_computer_tech', 'Радіофізики та комп’ютерних технологій'), ('computer_system', 'Радіоелектронних і комп’ютерних систем'), ('optoelec_it', 'Оптоелектроніки та інформаційних технологій')], max_length=50, null=True),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='interests',
        ),
        migrations.AddField(
            model_name='teacher',
            name='interests',
            field=models.ManyToManyField(blank=True, to='main.interest'),
        ),
    ]