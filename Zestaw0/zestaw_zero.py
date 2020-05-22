import pandas as pd
#df = pd.read_csv("./train.tsv")
#nie wszystkie kolummny i wiersze są widoczne
#Dlatego musimy zastosować poniższe:

#wyswietlanie wszystkich wierszy:
pd.set_option('display.max_rows', 10)
#wyświetlenie wszystkich kolumn (ale kolumny nie wyswietlają się w jednym wierszu):
pd.set_option('display.max_columns', None)
#kolumny wyświetlają sie w jednym wierszu (ale długi tekst zostaje ucięty);
pd.set_option('display.width', None)
#wyświetla się cały tekst we wszystkich kolumnach:
pd.set_option('display.max_colwidth', None)
#wyrownanie tekstu do lewej strony:
#pd.set_option('display.max_colwidth', -1)

#Wczytanie pliku
df = pd.read_csv("./train.tsv",delimiter='\t') #separator, podzielenie lini tekstu, znak dzielący Tab

#nazwy kolumn:
nazwyKolumn = ['Cena', 'Liczba_pokoi', 'Powierzchnia', 'Piętro', 'Lokalizacja', 'Opis']
df.columns = nazwyKolumn

#wypisanie wybranej kolumny:
print(df['Lokalizacja'])

#wypisanie dwóch wybranych kolumn:
dwie=df[['Cena','Piętro']]
print(dwie)

#wypisanie całości:
print(df)

#info() - otrzymujemy listę kolumn z typami danych i zużyciem pamięci:
print(df.info())

















