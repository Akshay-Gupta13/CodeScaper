# Generated by Django 4.1.10 on 2023-07-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('problem_name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=10)),
                ('code', models.TextField()),
                ('verdict', models.CharField(max_length=120)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='test_case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tc_input', models.CharField(max_length=200)),
                ('tc_output', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problem_id', models.IntegerField(primary_key=True, serialize=False)),
                ('problem_name', models.CharField(max_length=200)),
                ('problem_description', models.TextField()),
                ('problem_difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=20)),
                ('problem_timelimit', models.IntegerField(default=2, help_text='in seconds')),
                ('problem_memorylimit', models.IntegerField(default=8, help_text='in MB')),
                ('test_cases', models.ManyToManyField(to='question.test_case')),
            ],
        ),
    ]
