import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#------------Zad.4-----------
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#pd.set_option('display.max_rows', None)

df_survey = pd.read_csv('survey_results_public.csv',usecols=['Respondent', 'Age', 'WorkWeekHrs'],index_col='Respondent')

#.dropna - Remove missing values.
#          Usuwa brakujące wartości /inplace -> Usunie NaN / Usunie wiersze, w których brakuje co najmniej jednego elementu.
df_survey.dropna(inplace=True)
print(df_survey)

#Określenie punktów dla wykresu:
#ro - red circle
plt.plot(df_survey['Age'], df_survey['WorkWeekHrs'], 'ro', markersize=1)
#Nazwanie osi X:
plt.xlabel('Age')
#Nazwanie osi Y:
plt.ylabel('Hours')
#Funkcja pokazująca wykres:
plt.show()




#-----------Zad.5-----------

df_survey_2 = pd.read_csv('survey_results_public.csv',usecols=['Respondent', 'Age', 'WorkWeekHrs', 'Gender'],index_col='Respondent')
df_survey_2.dropna(inplace=True)
print(df_survey_2)

#.loc -> uzyskuje dostęp do grupy wierszy i kolumn według etykiet
#        lub tablicy boolowskiej w podanej tabeli danych.
#Kolumna: 'Gender', gdzie: 'Man' :
df_survey_2_man = df_survey_2.loc[df_survey_2['Gender'] == 'Man']
#Określenie punktów dla wykresu:
plt.plot(df_survey_2_man['Age'], df_survey_2_man['WorkWeekHrs'], 'ro', markersize=0.5)
#Nazwanie osi X:
plt.xlabel('Age')
#Nazwanie osi Y:
plt.ylabel('Hours')
#Tytuł wykresu:
plt.title('Man')
#Funkcja pokazująca wykres:
plt.show()

#Kolumna 'Gender", gdzie: 'Woman' :
df_survey_2_woman = df_survey_2.loc[df_survey_2['Gender'] == 'Woman']
plt.plot(df_survey_2_woman['Age'], df_survey_2_woman['WorkWeekHrs'], 'ro', markersize=0.5)
plt.xlabel('Age')
plt.ylabel('Hours')
plt.title('Woman')
plt.show()





