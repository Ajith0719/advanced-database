import pandas as pd
import sqlite3

df = pd.read_csv("title.basics.tsv", sep="\t")
connection = sqlite3.connect("imdb.db")
chunksize = 10000
i = 1
for chunk in pd.read_csv("title.basics.tsv", sep="\t", chunksize=chunksize):
    print("chunk # ",i)
    i = i + 1
    chunk.to_sql("title_basics", connection, if_exists="append", index=False)
connection.close()
