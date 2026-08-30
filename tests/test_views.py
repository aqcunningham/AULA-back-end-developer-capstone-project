from django.test import TestCase
from myapp.models import Reservation
from myapp.serializers import ReservationSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group

class ReservationViewTest(TestCase):
    def setUp(self):
        self.managers_group = Group.objects.create(name='managers')
        self.waiters_group = Group.objects.create(name='waiters')

        self.manager_user = User.objects.create_user(username='aulamanager', password='aulamanager123')
        self.manager_user.groups.add(self.managers_group)

        self.waiters = User.objects.create_user(username='kylewaiter', password='kylewaiter123')
        self.waiters.groups.add(self.waiters_group)

        self.reservation = Reservation.objects.create(
            first_name='Test Guest',
            reservation_date='2026-09-01',
            reservation_slot=18,
            number_of_guests=2,
            occasion='Birthday'
        )

    def test_waiter_cannot_delete_reservation(self):
        client = APIClient()
        client.force_authenticate(user=self.waiters)
        response = client.delete(f'/make_reservation/drf/{self.reservation.id}/')
        self.assertEqual(response.status_code, 403)

    def test_manager_can_delete_reservation(self):
        client = APIClient()
        client.force_authenticate(user=self.manager_user)
        response = client.delete(f'/make_reservation/drf/{self.reservation.id}/')
        self.assertEqual(response.status_code, 204)

    def test_waiter_can_create_reservation(self):
        client = APIClient()
        client.force_authenticate(user=self.waiters)
        response = client.post('/make_reservation/drf/', {
            'first_name': 'New Guest',
            'reservation_date': '2026-09-02',
            'reservation_slot': 19,
            'number_of_guests': 4,
            'occasion': ''
        })
        self.assertEqual(response.status_code, 201)