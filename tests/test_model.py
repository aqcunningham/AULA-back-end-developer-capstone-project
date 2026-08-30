# test file
from django.test import TestCase
from myapp.models import Reservation

class ReservationModelTest(TestCase):
    def test_reservation_str(self):
        reservation = Reservation.objects.create(
            first_name='John Doe',
            reservation_date='2026-09-01',
            reservation_slot=18,
            number_of_guests=2
        )
        self.assertEqual(str(reservation), 'John Doe')