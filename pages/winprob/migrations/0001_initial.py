# Generated by Django 3.0.6 on 2020-05-30 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('fbrefid', models.CharField(max_length=10)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winprob.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('season', models.IntegerField()),
                ('competition', models.CharField(choices=[('cl', 'UEFA Champions League'), ('el', 'UEFA Europa League')], max_length=5)),
                ('stage', models.CharField(choices=[('cl-0q-1fqr', 'Champions League First Qualifying Round'), ('cl-0q-2sqr', 'Champions League Second Qualifying Round'), ('cl-0q-3tqr', 'Champions League Third Qualifying Round'), ('cl-0q-4po', 'Champions League Qualifying Play-off Round'), ('cl-1k-1r16', 'Champions League Round of 16'), ('cl-1k-2qf', 'Champions League Quarterfinals'), ('cl-1k-3sf', 'Champions League Semifinals'), ('el-0q-0pre', 'Europa League Preliminary Qualifying Round'), ('el-0q-1fqr', 'Europa League First Qualifying Round'), ('el-0q-2sqr', 'Europa League First Qualifying Round'), ('el-0q-3tqr', 'Europa League First Qualifying Round'), ('el-0q-4po', 'Europa League Qualifying Play-off Round'), ('el-1k-1r32', 'Europa League Round of 32'), ('el-1k-2r16', 'Europa League Round of 16'), ('el-1k-3qf', 'Europa League Quarterfinals'), ('el-1k-4sf', 'Europa League Semifinals')], max_length=15)),
                ('tieid', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=100)),
                ('aggscore', models.CharField(max_length=10)),
                ('score_leg1', models.CharField(max_length=10)),
                ('score_leg2', models.CharField(max_length=10)),
                ('away_goals_rule', models.BooleanField()),
                ('after_extra_time', models.BooleanField()),
                ('penalty_kicks', models.BooleanField()),
                ('has_events', models.BooleanField()),
                ('has_odds', models.BooleanField()),
                ('has_invalid_match', models.BooleanField()),
                ('in_progress', models.BooleanField()),
                ('team1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='winprob.Team')),
                ('team2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='winprob.Team')),
                ('winning_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning_team', to='winprob.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
