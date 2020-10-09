# Create your tests here.
import datetime

from django.test import TestCase

from eviteapi.models import Event


class EventTestCase(TestCase):
    def testPost(self):
        event = Event(event_id="evt100001", name="Test Event", location="Tokyo", start_time=datetime.datetime.now(),
                      end_time=datetime.datetime.now() + datetime.timedelta(days=1, hours=3))
        self.assertEqual(event.event_id, "evt100001")
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.location, "Tokyo")
