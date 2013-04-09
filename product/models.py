from django.db import models
from django import forms
from django.forms import ModelForm
from  django.core.validators import MinValueValidator, ValidationError
from decimal import Decimal 

class Items(models.Model):
	name = models.CharField(max_length=50, blank=False)
	price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, validators=[MinValueValidator(Decimal('0.01'))])
	photo = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=500, blank=False)
	
	def __unicode__(self):
         return self.name
	
    
	
class Items_F(ModelForm):
	class Meta:
		model = Items	
        		
        def cleaned_price(self):
            data= self.cleaned_price['price']
            if data <= 0:
               raise forms.ValidationError("Price can't be a negative number")
            return data
		
        def cleaned_photo(self):
            data = self.cleaned_photo['photo']
            if data == None:
               raise forms.ValidationError("This field can't be empty")
            return data
		
		
        def cleaned_description(self):
            data = self.cleaned_description['description']
            if data == None:
               raise forms.ValidationError("This field can't be empty")
            return data