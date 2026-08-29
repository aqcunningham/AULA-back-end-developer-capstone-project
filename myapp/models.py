from django.db import models

# a table for Reservations aka Booking, from the last lab
class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    # its for the time:
    reservation_slot = models.SmallIntegerField(default=10)
    number_of_guests = models.IntegerField(default=2)
    occasion = models.CharField(max_length=200, blank=True)
    def __str__(self): 
        return self.first_name


# a table for Menu
class Menu(models.Model):
    item_name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    inventory = models.IntegerField(default=5)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    def __str__(self):     
        return self.item_name
    # a fucntion created to be tested in the Unit later:
    def get_item(self):
        return f'{self.item_name}: {str(self.price)}'
    


# a table/model for user comment
class Reviews(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	comment = models.CharField(max_length = 1000)
    	# __str__ is a dunder method is just about how the object displays itself when printed or shown in Django admin

	def __str__(self): 
          return self.first_name


    