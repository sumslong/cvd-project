'''
Constructing the search terms to be fed into the crawlers 
'''

def constructing_search_terms(sys_bp, sex, BMI, smoke):

    search_terms = "heart disease"
    search_list = ["heart disease"]
        
    if sys_bp > 130:
        search_terms = search_terms + " high blood pressure"
        search_list.append("high blood pressure")
        
    if sex == "female":
        search_terms = search_terms + " female" 
        search_list.append("female")
        
    if BMI >= 25: 
        search_terms = search_terms + " physical activity"
        search_list.append("physical")
        
    if smoke == "1":
        search_terms = search_terms + " smoking"
        search_list.append("smoking")
        
    return search_terms, search_list