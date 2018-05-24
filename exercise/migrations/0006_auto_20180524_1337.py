# Generated by Django 2.0.5 on 2018-05-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20180523_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('email_from', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.IntegerField(choices=[(0, 'phishing'), (1, 'regular')])),
                ('content', models.TextField(blank=True, null=True)),
                ('attachments', models.ManyToManyField(to='exercise.ExerciseAttachment')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseEmailReplies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='profile_definition_json',
        ),
        migrations.AddField(
            model_name='exerciseemail',
            name='replies',
            field=models.ManyToManyField(to='exercise.ExerciseEmailReplies'),
        ),
    ]
