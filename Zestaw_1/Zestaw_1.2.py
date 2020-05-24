import pandas as pd

#Wczytanie pliku train:
df = pd.read_csv("./train.tsv",delimiter='\t')
#Nadanie nazw kolumn:
nazwyKolumn = ['Cena', 'Liczba_pokoi', 'Powierzchnia', 'Piętro', 'Lokalizacja', 'Opis']
df.columns = nazwyKolumn

#Wczytanie pliku description:
description = pd.read_csv("./description.csv", sep=",")

#Połączenie danych z dwóch tabel - opis zależny od piętra:
#pd.merge(frame_1, frame_2, left_on='left_frame_kolumn_name', right_on='right_frame_kolumn_name')
#plik 'train' wiersz 'Piętro' -> łączenie z plikiem 'description' wiersz 'liczba'
#outer -> łączy wszystkie wiersze dla lewej i prawej tabeli danych,
#         wypisuje NaN, gdy nie ma zgodnych wartości w wierszach.
#indicator -> ustawiony na True wypisze skąd pochodzi każdy wiersz w danych
join = pd.merge(df, description, left_on='Piętro', right_on='liczba', how='outer', indicator=True)

#Zachowa wiersze w lewej tabeli:
#join = pd.merge(df, description, left_on='Piętro', right_on='liczba', how='left', indicator=True)

#Zapisanie wyniku do pliku out2:
join.to_csv("./out2.csv")

print(join)



