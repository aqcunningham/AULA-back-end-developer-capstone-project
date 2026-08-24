from django.test import TestCase
from myapp.models import Menu

# testing get_item fucntion, from the model
class MenuTest(TestCase):
	def test_get_item(self):
		item = Menu.objects.create(item_name="IceCream", price=80, inventory=100)
		itemstr = item.get_item()
		
		self.assertEqual(itemstr, "IceCream: 80")
