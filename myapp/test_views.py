from django.test import TestCase
from myapp.models import Menu
from myapp.serializers import MenuSerializer
from django.contrib.auth.models import User

# checks if data that API endpoints return, match the manually serialzied queryset
class MenuViewTest(TestCase):
	def setUp(self):		
		self.user = User.objects.create_user(username="tester", password="tester123")
		self.item1 = Menu.objects.create(item_name="Pasta", price=20)
		self.item2 = Menu.objects.create(item_name="Salad", price=15)

	def test_getall(self):
		self.client.login(username="tester", password="tester123")
		response = self.client.get('/api/menu/')
		menu_items = Menu.objects.all()
		serializer = MenuSerializer(menu_items, many = True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, 200)