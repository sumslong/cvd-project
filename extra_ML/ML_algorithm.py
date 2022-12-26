import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier


df_raw = pd.read_csv('cardio_train.csv', sep = ';')
df_raw["BMI"] = (df_raw['weight']) / (df_raw['height']/100)**2

# Cleaning the data
df = df_raw[(df_raw["ap_hi"] > 50) & (df_raw["ap_hi"] < 200) & \
            (df_raw["BMI"] > 10) & (df_raw["BMI"] < 40)]


def random_forest():
    '''
    Construct a random forest machine learning algorithm to
    predict whether someone is likely to have heart disease.
    This model was used because is had the best performance.
    '''
    
    feature_names = ['age', 'BMI', 'ap_hi']

    X = np.array(df.loc[:, feature_names])
    y = np.array(df.loc[:, 'cardio'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    classifier = RandomForestClassifier(n_estimators=1000)
    
    rf = classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    # To store the model
    pickle.dump(rf, open('car_train.pkl', 'wb'))


def support_vector_machine():
    '''
    Construct a support vector machine model to predict whether someone
    is likely to have heart disease.
    This model was NOT used due to worse performance than the random
    forest algorithm.
    '''

    X = np.array(df.loc[:, ['age', 'BMI', 'ap_hi']])
    y = np.array(df.loc[:, 'cardio'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    classifier = SVC(kernel = 'linear')

    svc = classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    #pickle.dump(svc, open('car_train.pkl', 'wb'))


def feature_importance(classifier, feature_names):
    '''
    Feature selection was accomplished by using the feature
    importance metric.
    '''

    # id;age;gender;height;weight;ap_hi;ap_lo;cholesterol;gluc;smoke;alco;active;cardio

    #feature_names = ['age', 'BMI', 'ap_hi', 'cholesterol', 'gender', 'smoke']
    
    #X = np.array(df.loc[:, feature_names])
    #y = np.array(df.loc[:, 'cardio'])

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
    
    #classifier = RandomForestClassifier(n_estimators=1000)
    
    #rf = classifier.fit(X_train, y_train)
    #y_pred = classifier.predict(X_test)

    feature_importance = pd.Series(classifier.feature_importances_,index=feature_names).sort_values(ascending=False)
    feature_importance




