import pandas as pd

def retrieve_stats_for_state(state, year=2020):
   '''
   Find mortality rate and number of deaths for a given state & year
 
   Inputs:
       m_data (pd DF) mortality data
       state (str) USPS state abbreviation
       year (int)
 
   Returns (tuple of int) mortality rate and number of deaths in a given state & year
   '''
   state_dict =  {'Alabama': 'AL', 
                  'Alaska': 'AK', 
                  'Arizona': 'AZ',
                  'Arkansas': 'AR', 
                  'California': 'CA', 
                  'Colorado': 'CO', 
                  'Connecticut': 'CT',
                  'Delaware': 'DE',
                  'Florida': 'FL', 
                  'Georgia': 'GA', 
                  'Hawaii': 'HI', 
                  'Idaho': 'ID', 
                  'Illinois': 'IL', 
                  'Indiana': 'IN', 
                  'Iowa': 'IA', 
                  'Kansas': 'KS', 
                  'Kentucky': 'KY', 
                  'Louisiana': 'LA', 
                  'Maine': 'ME', 
                  'Maryland': 'MD', 
                  'Massachusetts': 'MA', 
                  'Michigan': 'MI', 
                  'Minnesota': 'MN', 
                  'Mississippi': 'MS', 
                  'Missouri': 'MO', 
                  'Montana': 'MT', 
                  'Nebraska': 'NE', 
                  'Nevada': 'NV', 
                  'New_Hampshire': 'NH',  
                  'New_Jersey': 'NJ', 
                  'New_Mexico': 'NM', 
                  'New_York': 'NY', 
                  'North_Carolina': 'NC', 
                  'North_Dakota': 'ND', 
                  'Ohio': 'OH', 
                  'Oklahoma': 'OK', 
                  'Oregon': 'OR', 
                  'Pennsylvania': 'PA', 
                  'Rhode_Island': 'RI', 
                  'South_Carolina': 'SC',
                  'South_Dakota': 'SD', 
                  'Tennessee': 'TN', 
                  'Texas': 'TX', 
                  'Utah': 'UT',
                  'Vermont': 'VT', 
                  'Virginia': 'VA', 
                  'Washington': 'WA', 
                  'West_Virginia': 'WV', 
                  'Wisconsin': 'WI', 
                  'Wyoming': 'WY'}
   m_data = pd.read_csv('map/mortality_data.csv')
   choose_row = m_data[(m_data.STATE == state_dict[state]) & (m_data.YEAR == year)]
   m_rate = choose_row.RATE.item()
   deaths = int(choose_row.DEATHS.item().replace(',', ''))
 
   return (m_rate, deaths)


def get_states_list():
    states_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New_Hampshire', 'New_Jersey', 'New_Mexico', 'New_York', 'North_Carolina', 'North_Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode_Island', 'South_Carolina', 'South_Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West_Virginia', 'Wisconsin', 'Wyoming']
    return states_list

def get_html_links():

    html_state_code = ['<a href="https://ibb.co/0mkKBw9"><img src="https://i.ibb.co/wBT7JvQ/Alabama.png" alt="Alabama" border="0"></a>',
                '<a href="https://ibb.co/9Vsq9Wh"><img src="https://i.ibb.co/k9QhgXJ/Alaska.png" alt="Alaska" border="0"></a>',
                '<a href="https://ibb.co/db8Z3sw"><img src="https://i.ibb.co/q0T64L3/Arizona.png" alt="Arizona" border="0"></a>',
                '<a href="https://ibb.co/mXL2mfW"><img src="https://i.ibb.co/4Y6Xchr/Arkansas.png" alt="Arkansas" border="0"></a>',
                '<a href="https://ibb.co/pxhzvCG"><img src="https://i.ibb.co/s2WwvLk/California.png" alt="California" border="0"></a>',
                '<a href="https://ibb.co/s22tfM7"><img src="https://i.ibb.co/SPPJj9S/Colorado.png" alt="Colorado" border="0"></a>',
                '<a href="https://ibb.co/mFx1T1K"><img src="https://i.ibb.co/sJBkRk4/Connecticut.png" alt="Connecticut" border="0"></a>',
                '<a href="https://ibb.co/8DYRHwg"><img src="https://i.ibb.co/6RXpkS0/Delaware.png" alt="Delaware" border="0"></a>',
                '<a href="https://ibb.co/XyWrw66"><img src="https://i.ibb.co/pW1BmNN/Florida.png" alt="Florida" border="0"></a>',
                '<a href="https://ibb.co/4FC8v13"><img src="https://i.ibb.co/Fhc5ZHC/Georgia.png" alt="Georgia" border="0"></a>',
                '<a href="https://ibb.co/2czngnL"><img src="https://i.ibb.co/p4H0J0s/Hawaii.png" alt="Hawaii" border="0"></a>',
                '<a href="https://ibb.co/8xF1MPL"><img src="https://i.ibb.co/DM304wH/Idaho.png" alt="Idaho" border="0"></a>',
                '<a href="https://ibb.co/gyy8GZH"><img src="https://i.ibb.co/dBBvS41/Illinois.png" alt="Illinois" border="0"></a>',
                '<a href="https://ibb.co/cNm7h9j"><img src="https://i.ibb.co/p3m9jTS/Indiana.png" alt="Indiana" border="0"></a>',
                '<a href="https://ibb.co/K0hz8Q7"><img src="https://i.ibb.co/LkRhsq6/Iowa.png" alt="Iowa" border="0"></a>',
                '<a href="https://ibb.co/T03w2mH"><img src="https://i.ibb.co/FYTh3gB/Kansas.png" alt="Kansas" border="0"></a>',
                '<a href="https://ibb.co/5hpSsLh"><img src="https://i.ibb.co/Kx4fVWx/Kentucky.png" alt="Kentucky" border="0"></a>',
                '<a href="https://ibb.co/3BqLbLh"><img src="https://i.ibb.co/Hnskykg/Louisiana.png" alt="Louisiana" border="0"></a>',
                '<a href="https://ibb.co/0t8f8LJ"><img src="https://i.ibb.co/q5XRX81/Maine.png" alt="Maine" border="0"></a>',
                '<a href="https://ibb.co/5xyz1Sd"><img src="https://i.ibb.co/TqSnw7Z/Maryland.png" alt="Maryland" border="0"></a>',
                '<a href="https://ibb.co/vcZr8Ct"><img src="https://i.ibb.co/grzXCbn/Massachusetts.png" alt="Massachusetts" border="0"></a>',
                '<a href="https://ibb.co/p2tH8Qc"><img src="https://i.ibb.co/Px72nMK/Michigan.png" alt="Michigan" border="0"></a>',
                '<a href="https://ibb.co/HYNjqmS"><img src="https://i.ibb.co/Bj49B8p/Minnesota.png" alt="Minnesota" border="0"></a>',
                '<a href="https://ibb.co/bJY4jDt"><img src="https://i.ibb.co/tXn0wFR/Mississippi.png" alt="Mississippi" border="0"></a>',
                '<a href="https://ibb.co/Zx0dyV6"><img src="https://i.ibb.co/cQjJz1c/Missouri.png" alt="Missouri" border="0"></a>',
                '<a href="https://ibb.co/vPPDRwn"><img src="https://i.ibb.co/xjj3dCT/Montana.png" alt="Montana" border="0"></a>',
                '<a href="https://ibb.co/rfRJfs3"><img src="https://i.ibb.co/BK5RKNG/Nebraska.png" alt="Nebraska" border="0"></a>',
                '<a href="https://ibb.co/N3VgZVG"><img src="https://i.ibb.co/j569g6j/Nevada.png" alt="Nevada" border="0"></a>',
                '<a href="https://ibb.co/2vDZv6r"><img src="https://i.ibb.co/1rDzrnN/New-Hampshire.png" alt="New-Hampshire" border="0"></a>',
                '<a href="https://ibb.co/qBNpSFH"><img src="https://i.ibb.co/7vnKfN3/New-Jersey.png" alt="New-Jersey" border="0"></a>',
                '<a href="https://ibb.co/TBGqBqL"><img src="https://i.ibb.co/RpK4p4y/New-Mexico.png" alt="New-Mexico" border="0"></a>',
                '<a href="https://ibb.co/0JXMJ0P"><img src="https://i.ibb.co/C0t70jx/New-York.png" alt="New-York" border="0"></a>',
                '<a href="https://ibb.co/fdbvTNS"><img src="https://i.ibb.co/hFkfTdM/North-Carolina.png" alt="North-Carolina" border="0"></a>',
                '<a href="https://ibb.co/vmzq99v"><img src="https://i.ibb.co/tcCKRRP/North-Dakota.png" alt="North-Dakota" border="0"></a>',
                '<a href="https://ibb.co/2dn0hmQ"><img src="https://i.ibb.co/KW0chRk/Ohio.png" alt="Ohio" border="0"></a>',
                '<a href="https://ibb.co/VvT11p4"><img src="https://i.ibb.co/zSZMMHv/Oklahoma.png" alt="Oklahoma" border="0"></a>',
                '<a href="https://ibb.co/sR331Pq"><img src="https://i.ibb.co/02JJ9Xr/Oregon.png" alt="Oregon" border="0"></a>',
                '<a href="https://ibb.co/tHdNNF7"><img src="https://i.ibb.co/10SppjD/Pennsylvania.png" alt="Pennsylvania" border="0"></a>',
                '<a href="https://ibb.co/1dm9NHy"><img src="https://i.ibb.co/YyLtSvn/Rhode-Island.png" alt="Rhode-Island" border="0"></a>',
                '<a href="https://ibb.co/xFRGmSq"><img src="https://i.ibb.co/qJP90MY/South-Carolina.png" alt="South-Carolina" border="0"></a>',
                '<a href="https://ibb.co/qnVzzpZ"><img src="https://i.ibb.co/FWC99zP/South-Dakota.png" alt="South-Dakota" border="0"></a>',
                '<a href="https://ibb.co/S3SpDGT"><img src="https://i.ibb.co/jrtF9sK/Tennessee.png" alt="Tennessee" border="0"></a>',
                '<a href="https://ibb.co/zr3dtYp"><img src="https://i.ibb.co/SPkSZ8b/Texas.png" alt="Texas" border="0"></a>',
                '<a href="https://ibb.co/Rcdqz1G"><img src="https://i.ibb.co/CQDfhqp/Utah.png" alt="Utah" border="0"></a>',
                '<a href="https://ibb.co/PTTxMk2"><img src="https://i.ibb.co/3ff1vKx/Vermont.png" alt="Vermont" border="0"></a>',
                '<a href="https://ibb.co/R6C2xsn"><img src="https://i.ibb.co/WzcnbM9/Virginia.png" alt="Virginia" border="0"></a>',
                '<a href="https://ibb.co/j6CbWFP"><img src="https://i.ibb.co/smTb6rd/Washington.png" alt="Washington" border="0"></a>',
                '<a href="https://ibb.co/nMxcc9g"><img src="https://i.ibb.co/TM9886v/West-Virginia.png" alt="West-Virginia" border="0"></a>',
                '<a href="https://ibb.co/pXtJWvB"><img src="https://i.ibb.co/ThVmKBx/Wisconsin.png" alt="Wisconsin" border="0"></a>',
                '<a href="https://ibb.co/sKWMbmy"><img src="https://i.ibb.co/tqLWQm8/Wyoming.png" alt="Wyoming" border="0"></a>']


def get_short_link():
    prefix = "https://ibb.co/"
    short_link_list = [
        '0mkKBw9',
'9Vsq9Wh',
'db8Z3sw',
'mXL2mfW',
'pxhzvCG',
's22tfM7',
'mFx1T1K',
'8DYRHwg',
'XyWrw66',
'4FC8v13',
'2czngnL',
'8xF1MPL',
'gyy8GZH',
'cNm7h9j',
'K0hz8Q7',
'T03w2mH',
'5hpSsLh',
'3BqLbLh',
'0t8f8LJ',
'5xyz1Sd',
'vcZr8Ct',
'p2tH8Qc',
'HYNjqmS',
'bJY4jDt',
'Zx0dyV6',
'vPPDRwn',
'rfRJfs3',
'N3VgZVG',
'2vDZv6r',
'qBNpSFH',
'TBGqBqL',
'0JXMJ0P',
'fdbvTNS',
'vmzq99v',
'2dn0hmQ',
'VvT11p4',
'sR331Pq',
'tHdNNF7',
'1dm9NHy',
'xFRGmSq',
'qnVzzpZ',
'S3SpDGT',
'zr3dtYp',
'Rcdqz1G',
'PTTxMk2',
'R6C2xsn',
'j6CbWFP',
'nMxcc9g',
'pXtJWvB',
'sKWMbmy',
    ]
    return short_link_list


def get_img_src(state):
    '''
    Gets the string needed for the HTML tag to render the image
    '''
    state_dash = state.replace('_', '-')

    states_list = get_states_list()
    index = states_list.index(state)
    short_link_list = get_short_link()
    
    href_str = "https://ibb.co/" + short_link_list[index]
    src_str = "https://i.ibb.co/" + short_link_list[index] + "/" + state_dash + ".png"

    return (href_str, src_str)



def get_state_link(state):
    states_list = get_states_list()
    html_links = get_html_links()
    index = states_list.index(state)
    state_html = html_links(index)

    return state_html

    