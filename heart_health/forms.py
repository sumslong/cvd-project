from random import choices
from turtle import width, window_height
from django import forms
from django.forms.widgets import NumberInput, RadioSelect, TextInput
from django.forms import TextInput, RadioSelect



class SurveyForm(forms.Form):
    '''
    Creates the Django form. Each field is customized to only allow the values that make sense for validation purposes. 
    '''
    
    name = forms.CharField(label='Name', max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px', 'class': 'form-control'}))
    
    sex_choices = [("male", "Male"), ("female", "Female")]
    sex = forms.ChoiceField(label='Sex', choices=sex_choices, widget = forms.RadioSelect(attrs = {"class": "inline"}))
    
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'style': 'height: 30px'}))

    height = forms.FloatField(help_text = "feet", min_value=4, max_value=7, widget=forms.NumberInput(attrs={'placeholder': 'Ex: 5.4', 'class': 'form-control', 'step': "0.1", 'style': 'width : 100px; height: 30px'}))

    weight = forms.IntegerField(help_text = "lbs", min_value=75, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control','style': 'width : 100px; height: 30px'}))

    sys_bp = forms.IntegerField(label='Systolic Blood Pressure', help_text = "mmHg", min_value=60, max_value=220,
             widget=forms.NumberInput(attrs={'placeholder': 'Normal is ~120', 'class': 'form-control','style': 'width : 120px; height: 30px'}))

    state_list = [('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'),
                ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'),
                ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'),
                ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'),
                ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'),
                ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'),
                ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'),
                ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New_Hampshire', 'New Hampshire'), 
                ('New_Jersey', 'New Jersey'), ('New_Mexico', 'New Mexico'), ('New_York', 'New York'), ('North_Carolina', 'North Carolina'),
                ('North_Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'),
                ('Pennsylvania', 'Pennsylvania'), ('Rhode_Island', 'Rhode Island'), ('South_Carolina', 'South Carolina'),
                ('South_Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'),
                ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West_Virginia', 'West Virginia'),
                ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')]
    state = forms.CharField(widget=forms.Select(choices=state_list, 
                            attrs={'placeholder': 'State', 'class': 'form-control', 
                                   'style': 'width : 160px; height: 40px'}))

    heredity_choices = [(1, "Yes"), (0, "No")]
    heredity = forms.ChoiceField(label='Do you have history of heart disease in your family?', choices=heredity_choices, 
                                 widget = forms.RadioSelect(attrs = {"class": "inline"}))

    smoke_choices = [(1, "Yes"), (0, "No")]
    smoke = forms.ChoiceField(label='Do you smoke regularly?', choices=smoke_choices, 
                              widget = forms.RadioSelect(attrs = {"class": "inline"}))

    active_choices = [(1, "Yes"), (0, "No")]
    active = forms.ChoiceField(label='Do you exercise regularly (>30 mins per day)?', choices=active_choices, 
                               widget = forms.RadioSelect(attrs = {"class": "inline"}))

    pre_existing_choices = [(1, "Yes"), (0, "No")]
    pre_existing = forms.ChoiceField(label='Do you have a pre-existing heart condition?', choices=pre_existing_choices, 
                                    widget = forms.RadioSelect(attrs = {"class": "inline"}))
    

    literacy_list = [('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('High', 'High')]
    literacy = forms.CharField(label='Literacy Level', widget=forms.Select(choices=literacy_list, 
                            attrs={'class': 'form-control', 'style': 'width : 160px; height: 40px'}))
    
        
    
    
