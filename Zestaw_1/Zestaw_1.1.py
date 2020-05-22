import pandas as pd

df = pd.read_csv("./train.tsv",delimiter='\t')
nazwyKolumn = ['Cena', 'Liczba_pokoi', 'Powierzchnia', 'Piętro', 'Lokalizacja', 'Opis']
df.columns = nazwyKolumn

#-----1)-------

#round()-function returns a floating point number
#that is a rounded version of the specified number with the specified number of decimals.
#mean()-Sample arithmetic mean of the provided data-set
#round - zaokragla liczbe do podanej ilosci miejsc po przecinku
#mean()-Zwraca średnią arytmetyczna zestawu danych
#Average/srednia:
average = round(df["Cena"].mean(), 0)

#wczytanie danych z pliku jako DataFrame:
df_avg = pd.DataFrame({average})

#Zapisanie danych do pliku out0.csv:
#index - indeksy/wiersze - False=bez nazw wierszy/indeksów
#header - nazwy kolumn -> False=bez nazw kolumn
df_avg.to_csv("./out0.csv", index=False, header=False)

#print(average)

#-----2)-------

df_m = df
df_m["Cena_za_metr_2"] = df_m["Cena"]/df_m["Powierzchnia"]

#zaokrąglenie ceny do dwoch miejsc:
df_m["Cena_za_metr_2"] = round(df_m["Cena_za_metr_2"], 2)

#Obliczenie średniej za metr:
average_price = (df_m["Cena_za_metr_2"].mean())

#Oferty z liczbą pokoi większą równą 3 i ceną za metr kwadrarowy  niższą niż średnia cena za metr kwadrarowy:
offers = df_m[(df_m["Liczba_pokoi"] >= 3) & (df_m["Cena_za_metr_2"] < average_price)]

#Zapisanie wymienionych kolumn dla części ofert do pliku out1.csv:
offers[['Liczba_pokoi', 'Cena', 'Cena_za_metr_2']].to_csv('out1.csv', header=False, index=False)

#print(df_m)
print(average_price)
print(offers)


