import risk_calculator

def get_risk_percent(risk_heart_disease):
    '''
    Gets the percent risk for heart disease (between 0 to 1) based
    on risk category level.

    Inputs:
        a string category risk level

    Returns:
        int (risk_percent)
        
    '''
    if risk_heart_disease == 'Low':
        risk_percent = 0.2
    elif risk_heart_disease == 'Low-Medium':
        risk_percent = 0.35
    elif risk_heart_disease == 'Medium':
        risk_percent = 0.5
    elif risk_heart_disease == 'Medium-High':
        risk_percent = 0.65
    else:
        risk_percent = 0.8

    return risk_percent


def optimal_screen_freq(risk_heart_disease, age):
    '''
    Find optimal frequency for screenings, given patient's risk of developing \
        severe heart disease and their age
  
    Inputs:
        risk_heart_disease (int): probability that patient will develop severe \
            heart disease in their lives, given their risk factors. \
                Decimal between 0 and 1
        age (int): patient's age
 
    Returns (str) recommendation for how often patient should get screened
    '''
    life_expectancy = 80.0
    cost_per_screen = 400.0
    cost_treat_heart_disease = 35000.0
    age_years = age/365.0
    
    risk_percent = get_risk_percent(risk_heart_disease)

    weighted_cost_heart_disease = cost_treat_heart_disease * risk_percent
    total_screenings = 0.5 * weighted_cost_heart_disease / cost_per_screen

    if age_years < 65:
        years_to_live = life_expectancy - age_years
    else:
        # Someone cannot have a negative years to live and if they are 
        # healthy/screened, they will keep living
        years_to_live = 15
    
    optimal_screenings_per_year = total_screenings / years_to_live
    optimal_freq_screened = 12.0 / optimal_screenings_per_year

    return "You should get tested every " + str(round((optimal_freq_screened / 12.0), 1)) + \
           " years."