"""Interface for health_app"""
# imports
# import pickle
# import logging
import sqlite3
import pandas as pd
import sys
import logging
import pandas as pd
import statsmodels as sm
import statsmodels.formula.api as smf
import sqlite3
from datetime import datetime



# with open("reg.pkl", "rb") as f:
#     reg = pickle.load(f)



# open connection to SQLite.db
dbName = "rest_server/medisch_centrum_randstad/db.sqlite3"

dbConnection = sqlite3.connect(dbName)

# query db and write to pd:
dfFromDB = pd.read_sql_query(f"SELECT * FROM {'coef'}", dbConnection)
# sql adds index, remove:
df = dfFromDB.drop('index', axis=1)
pd.set_option('display.max_columns', 10)
# print(df.head(12))


# gdpr check. are we allowed to save this persons current input numbers?
# name is not asked to make the data GDPR proof. 

gdpr_check = input('Please ask if the patient grants permission to save the input of the data reguarding their current habits in accordance with the GDPR. If permission is granted type: Yes : ').title()

if gdpr_check == 'Yes':
    print ('This sessions patients initial data will be saved')
    client_nr = input ('Enter the patient nr : ').title()
    
    
else:
    print ('No data will be saved this session')






# input safeguarding

#hide errors, scary for the user xD
sys.tracebacklimit = 0 

# input safeguarding


def inputDigit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    inputNum = None
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)
        logging.debug(inputStr)

        if inputStr.isdigit():
            inputNum = float(inputStr)

            if inputNum in acceptableRange:
                return inputNum

        i += 1

    return None
# acceptableRange = range(0, 200)
# age = int(inputDigit("Age [18 - 118]: ", acceptableRange))
# logging.debug(f"age : {age}")

# acceptableRange_genetic = range(50,121)
# acceptableRange_length = range(140,221)
# acceptableRange_mass = range(40,171)
# acceptableRange_alcohol = range(0,21)
# acceptableRange_sugar = range(0,21)
# acceptableRange_smoking = range(0,41)
# acceptableRange_exercise = range(0,9)

# genetic = int(inputDigit("Genetic age in years [50 - 120]: ", acceptableRange_genetic))
# length = int(inputDigit("Length in cm [140 - 220]: ", acceptableRange_length))
# mass = int(inputDigit("Mass in kg [40 - 170]: ", acceptableRange_mass))
# alcohol = int(inputDigit("Alcohol consumption in glasses per day [0 - 20]: ", acceptableRange_alcohol))
# sugar = int(inputDigit("sugar consumption in cubes per day [0 - 20]: ", acceptableRange_sugar))
# smoking = int(inputDigit("Smoking in sigarettes per day [0 - 40]: ", acceptableRange_smoking))
# exercise = int(inputDigit("Exercise in hours per day [0 - 8]: ", acceptableRange_exercise))
# divider = pow(length/100, 2) if length >0 else None
# bmi = round(mass/divider)
# logging.debug(f'bmi: {bmi}')

# genetic = int(77)
# length = int(177) 
# mass = int(77)
# alcohol = int(2)
# sugar = int(2)
# smoking = int(2)
# exercise = int(2)
# divider = pow(length/100, 2) if length >0 else None
# bmi = round(mass/divider)

# # lifespan_predict = reg.predict([[genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]])
# # print(lifespan_predict)
# # df = pd.DataFrame(data=[pi, e, phi])
# # df_input= pd.DataFrame(data=['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise', 'bmi'], [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi])
# # print (df_input.head)
# # input= [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]
# # print (input)
# # Python code demonstrate creating
# # DataFrame from dict narray / lists
# # By default addresses.
  
# create df_q to have the values for the input questions to be asked. 
data_questions = {'feature': ['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise'],
        'acc_min': [50,140,40,0,0,0,0],
        'acc_max': [121,221,171,21,21,41,9],
        'per':['age in years','in cm','in kg','consumption in glasses per day',
               'consumption in cubes per day','in sigarettes per day','in hours per day'] }

# Create DataFrame
df_q = pd.DataFrame(data_questions) 

# print (df_q)
# create the function to ask the question per 'feature'
def input_q(name):
    min,max, per = df_q.loc[df_q['feature'] == name, ['acc_min','acc_max', 'per']].values[0]
    return int(inputDigit(f"Please enter, {name} {per} in the range: {min}-{max-1} ", range(min,max)))
    
# print()
# genetic='genetic'
# test = input_q (genetic)
# print (test)
# initialize data of lists.
data = {'feature': ['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise', 'bmi'],
        'input_1': [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]}
  
# Create DataFrame
df_input = pd.DataFrame(data)

for n in df_q['feature']:
    
    df_input['input_1'][n] = input_q(n)

# genetic = input_q ('genetic')
# length = input_q ('length')
# mass = input_q ('mass')
# alcohol = input_q ('alcohol')
# sugar = input_q ('sugar')
# smoking = input_q ('smoking')
# exercise = input_q ('exercise')
divider = pow(df_input['length'][1]/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')
  


  
# # Print the output.
# print(df_input)



# multiply the rows of df and df_input for the relevant row. add the interceptor where the data crosses the y-axis. 
lifespan_predicted = int(sum(df_input['input_1'].multiply(df['coef']))+ df['intercept'][0])

print(f'the predicted lifespan is: {lifespan_predicted}')


# create df to be saved and save it in SQL
# create date
date = datetime.now().strftime("%Y-%m-%d")

if gdpr_check == 'Yes':
    data_to_save = {'feature': ['client_nr','date','lifespan_predicted','genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise'],
        f'{client_nr}_{date}': [client_nr, date, lifespan_predicted, genetic, length, mass, alcohol, sugar, smoking, exercise]}

    df_to_SQL = pd.DataFrame(data_to_save)

    print (df_to_SQL)
# df_save_to_SQLlite = 
