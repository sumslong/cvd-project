
Welcome to our cardiovascular health project!
Authors: Beatrice Katsnelson, Elise Katsnelson, Maria Tamayo, and Summer Long

1. The project consists of many parts, which are explained in the 
   'Project_Explanation.pdf' file. Please read this file to better understand
   our project.

2. Below are the instructions for how to run our project:

   1. From the base directory (/cvd-group-project/), navigate to the heart_health_site
   directory (cd heart_health_site)

   2. Pip install commands (may need to install something else that we all had installed 
      on our machines, but this should be comprehensive)
      a. pip install statsmodel
      b. pip install spacy
      c. python3 -m spacy download en_core_web_sm (please ensure to run this command)
      d. pip install textstat
      e. pip install lxml

   3. To run the site, enter the command: 'python3 manage.py runserver' from the 
      heart_health_site directory. You will receive a page not found (404) error -- do not worry! Add /heart_health to the end of the URL to view our site.
   
   4. Enjoy!


3. Below is an outline for all relevant files and a map of their location (a more
   extensive explanation is provided in the 'Project_Explanation.pdf' document)

   1. /
      1. ML_algorithm.py: Code for machine learning algorithm and feature selection
      2. ML_R.md: R code for ML algorithm design
      3. heart_health_site directory: The Django project, as well as the rest of
         the code, rests in this directory
      4. 'Project_Explanation.pdf': Explanation of project

   2. /heart_health_site
      1. cardio_train.csv: Dataset of 70,000 people with the target variable being (1) heart disease or (0) no heart disease

      2. car_train.pkl: pkl file that stores the machine learning model weights and parameters

      3. extra_ML directory: Extra code for ML feature selection and model selection
         1. ML_algorithm.py: Code for machine learning algorithm and feature selection
         2. ML_R.md: R code for ML algorithm design

      4. risk_calculator.py: Loads the dataset, creates and dumps the machine learning model, runs two proportion z-tests to obtain relevant risk factors, and obtain the risk factor based on a weighted points system

      5. risk_factors.pkl: A list of risk factors from the 70,000 people data set obtained from statistical testing

      6. state_map.py: Gets the html links and mortality data to render the map based on data from the mortality data csv file

      7. map directory
         1. map.py: Creates a geopandas map based on mortality data, outlines the state, and saves map to .png file
         2. mortality_data.csv: CDC dataset that records the number of deaths and death rate (number of deaths per 100,000 total population) by state by year
         3. t1_2021_us_state: includes the shapefile for US states, provided by the US Census Bureau

      8. econ_model.py: Performs the cost-benefit analysis based on the user's risk to output a screening frequency recommendation

      9. survey_data.pkl: Stores the data that the user inputs as a dictionary in a pkl file

      10. searchterms.py: Obtains the relevant search terms based on the user's input

      11. pubmedcrawler.py: Crawls PubMed with customized search terms based on the user's input

      12. googlescholarcrawler.py: Crawls Google Scholar with customized search terms based on the user's input

      13. webmedcrawler.py: Crawls WebMD with customized search terms based on the user's input

      14. mayocliniccrawler.py: Crawls Mayo Clinic with customized search terms based on the user's input
      
      15. nlpgradelevel.py: Performs natural language processing to rank difficulty level, as well as regular expressions for relevancy score. 
         PLEASE NOTE: we have found that (presumably due to different research guidelines in different countries), a lot of the articles are from Asian and African countries, despite relevant search terms.

      16. heart_health directory: Contains all the Django files

      17. heart_health_site directory: Contains settings
   
   3. /heart_health_site/heart_health
      1. forms.py: Creates the Django form. Each field is customized to only allow the values that make sense for validation purposes.
      2. views.py: Renders views for the web pages and loads, stores, and modifies the user's data from the form
      3. states directory: contains files for rendering the map
      4. static/heart_health directory: contains the state_maps directory with all the state map images. We decided to pre-generate the images so as to decrease run time as much as possible (and the image is selected based on the user's entered location)
      5. templates/heart_health directory: contains all the HTML files
   
   4. /heart_health_site/heart_health/templates/heart_health
      1. index.html: Renders welcome screen
      2. survey.html: Renders survey screen with form
      3. outcome.html: Renders main results / outcome page
      4. education.html: Renders educational resources page


