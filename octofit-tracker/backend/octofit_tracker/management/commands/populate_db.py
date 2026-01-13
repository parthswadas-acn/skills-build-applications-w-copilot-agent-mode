from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='dc')

        # Activities
        Activity.objects.create(user=ironman.email, type='run', duration=30, date='2026-01-10')
        Activity.objects.create(user=captain.email, type='cycle', duration=45, date='2026-01-11')
        Activity.objects.create(user=batman.email, type='swim', duration=25, date='2026-01-12')
        Activity.objects.create(user=superman.email, type='fly', duration=60, date='2026-01-13')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=85)

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='marvel')
        Workout.objects.create(name='Flying drills', description='Aerial skills', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with superhero test data'))
