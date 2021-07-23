import os
import pandas

os.listdir()
df_csv = pandas.read_csv("supermarkets.csv")
print(df_csv)

df_json = pandas.read_json("supermarkets.json")
df_json = df_json.set_index("Address")
#Moves the "Address" column as index
print(df_json)

df_excel = pandas.read_excel("supermarkets.xlsx", sheet_name = 0)
print(df_excel.loc["2":"3", "Address":"City"])

df_commas_txt = pandas.read_csv("supermarkets-commas.txt")
print(df_commas_txt.iloc[1:3, 1:3])

df_semicolons_txt = pandas.read_csv("supermarkets-semi-colons.txt", sep = ";")
df_semicolons_txt = df_semicolons_txt.drop(2, 0)
print(df_semicolons_txt)

df_noHeader_addColumns_addIndex = pandas.read_csv("supermarkets.csv", header = None)
df_noHeader_addColumns_addIndex.columns = ["ID", "Address", "City", "ZIP", "Country", "Name", "Employees"]
print(df_noHeader_addColumns_addIndex)
