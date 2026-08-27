from django import forms
from .models import Reviews, Menu, Reservation

# forms in general as a part of Django, manages user interaction, HTML generation, browser input validaiton

class ReservationForm(forms.ModelForm):
	first_name = forms.CharField(label='Name')
	reservation_slot = forms.IntegerField(label = 'Reservation Time')
	number_of_guests = forms.IntegerField(label = 'Guests', initial = 2, min_value=2)
	occasion = forms.CharField(
        label='What are we celebrating?',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3})
    )	
	class Meta:
		model = Reservation
		fields = '__all__'



class Reviews(forms.ModelForm):
	class Meta:
		model = Reviews
		fields = '__all__'

# the model form below is a better approach than was suggested in the lab, that was redundant
class MenuForm(forms.ModelForm):
	class Meta:
		model = Menu
		fields = '__all__'


