from django.test import TestCase, Client
from django.contrib.auth.models import User
from nwalsdev.meetup.models import Location, Meetup
from datetime import timedelta
from django.utils import timezone

class TestNwalsdev(TestCase):
    def setUp(self):
        test_location = Location(
            name="City Hardware",
            address="123 Main Street"
        )
        test_location.save()
        test_meetup = Meetup(
            title="Coders Lunch",
            location=test_location,
            start_time=timezone.now()+timedelta(days=1)
        )
        test_meetup.save()
        test_user = User(username="joe")
        test_user.set_password('password')
        test_user.save()
        self.client = Client()

    def test_home_public(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "City Hardware")

    def test_home_authenticated(self):
        self.client.login(username='joe', password='password')
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "City Hardware")
