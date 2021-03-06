# Generated by Django 2.2.5 on 2019-10-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0011_exercise_copied_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseemailproperties',
            name='release_codes',
            field=models.ManyToManyField(blank=True, help_text='Accepted codes.      Participants, who have been intercepted, will need to provide one of the selected codes      to proceed with the exercise.', to='exercise.ExerciseWebPageReleaseCode'),
        ),
    ]
