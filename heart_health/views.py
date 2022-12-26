from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django import forms
from .forms import SurveyForm
from datetime import date
import risk_calculator
import econ_model
import pubmedcrawler
import googlescholarcrawler
import mayocliniccrawler
import webmdcrawler
import state_map
from django.template import RequestContext
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest #pip install statsmodels in order to run this

'''
Renders views for the web pages and loads, stores, and modifies the user's data from 
the form in the dictionary 'cd', which stands for 'cleaned data'
'''


def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            weight = float(cd['weight']) * 0.453592 #converts weight from pounds to kgs
            height = float(cd['height']) * 0.3048 #converts height from feet to meters
            BMI =  round(weight / (height)**2, 2)
            cd['BMI'] = BMI
            cd.save()
            return render(request, 'heart_health/outcome.html', cd)
    else:
        form = SurveyForm()
    return render(request, 'heart_health/survey.html', {'form': form})
    

def index(request):
    return render(request, 'heart_health/index.html')


def outcome(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            weight = float(cd['weight']) * 0.453592 #converts weight from pounds to kgs
            height = float(cd['height']) * 0.3048 #converts height from feet to meters
            BMI =  round(weight / (height)**2, 2)            
            cd['BMI'] = BMI

            age = (date.today() - cd['birth_date']).days
            cd['age'] = age
            
            risk_factors = risk_calculator.get_risk_factors()
            cd['risk_score'] = risk_calculator.predicting_risk(risk_factors, cd['age'], cd['BMI'], cd['sys_bp'], cd['smoke'], cd['active'], cd['heredity'], cd['pre_existing'])

            cd['screening_rec'] = econ_model.optimal_screen_freq(cd['risk_score'], cd['age'])

            cd['BMI_rank'] = risk_calculator.rank_BMI(cd['BMI'])
            
            cd['risk_str'] = risk_calculator.get_risk_string(cd)

            #Getting each of the articles
            cd['article_list'] = pubmedcrawler.get_articles_and_abstracts(cd['sys_bp'], cd['sex'], cd['BMI'], cd['smoke'], cd['literacy'])
            cd['article1'] = cd['article_list'][0]
            cd['article2'] = cd['article_list'][1]
            cd['article3'] = cd['article_list'][2]
            cd['article4'] = cd['article_list'][3]
            cd['article5'] = cd['article_list'][4]

            cd['gs_links'] = googlescholarcrawler.google_scholar_links(cd['sys_bp'], cd['sex'], cd['BMI'], cd['smoke'])
            cd['mayo_links'] = mayocliniccrawler.links_from_search(cd['sys_bp'], cd['sex'], cd['BMI'], cd['smoke'])
            cd['webmd_links'] = webmdcrawler.links_from_search(cd['sys_bp'], cd['sex'], cd['BMI'], cd['smoke'])

            cd['href_state'], cd['img_src_state'] = state_map.get_img_src(cd['state'])
            cd['map_path'] = "heart_health/state_maps/" + cd['state'] + ".png" 
            cd['mortality'], cd['deaths'] = state_map.retrieve_stats_for_state(cd["state"])

            pickle.dump(cd, open('survey_data.pkl', 'wb'))
                
            return render(request, 'heart_health/outcome.html', cd)
    else:
        cd = pickle.load(open('survey_data.pkl', 'rb'))
        return render(request, 'heart_health/outcome.html', cd)

    
def education(request):
    cd = pickle.load(open('survey_data.pkl', 'rb'))
    cd['article_list'] = pubmedcrawler.get_articles_and_abstracts(cd['sys_bp'], cd['sex'], cd['BMI'], cd['smoke'], cd['literacy'])
    cd['article1'] = cd['article_list'][0]
    cd['article2'] = cd['article_list'][1]
    cd['article3'] = cd['article_list'][2]
    cd['article4'] = cd['article_list'][3]
    cd['article5'] = cd['article_list'][4] 

    pickle.dump(cd, open('survey_data.pkl', 'wb'))

    return render(request, 'heart_health/education.html', cd)

