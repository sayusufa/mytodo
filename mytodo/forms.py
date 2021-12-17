from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):

    Date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing",),)

    task = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task...', 'class': 'input is-small', 'class': 'column is-half'}), label='Task')
    Date = forms.DateField(widget= forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day",),))
    time_todo = forms.TimeField(widget= forms.TimeInput(attrs={'placeholder':'hh:mm', 'class': 'time is-small', 'class': 'column is-half'}), label='Time')

    class Meta:
        model = Task
        fields = ['task', 'Date', 'time_todo']

class UpdateForm(forms.ModelForm):
    task = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task...', 'class': 'input is-small', 'class': 'column is-half'}), label='Task')
    Date = forms.DateField(widget= forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day",),))
    time_todo = forms.TimeField(widget= forms.TimeInput(attrs={'placeholder':'hh:mm', 'class': 'time is-small', 'class': 'column is-half'}), label='Time')
    is_executed = forms.BooleanField(widget= forms.CheckboxInput(attrs={'class': 'checkbox'}), label='Status: Executed/Unexecuted')

    class Meta:
        model = Task
        fields = ['task', 'Date', 'time_todo', 'is_executed']