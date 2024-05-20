from django import forms

from .models import Event, Category

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'data', 'place', 'description', 'likes', 'category')



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


