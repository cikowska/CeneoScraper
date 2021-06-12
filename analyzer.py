from os import listdir
from numpy import arange
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


pd.set_option("display.max_columns", None)

print(*[file_name.split(".")[0] for file_name in listdir("reviews")], sep="\n")
product_id = input("Podaj identyfikator produktu: ")
#product_id = "99756635"
reviews = pd.read_json(f"reviews/{product_id}.json")
reviews_count = reviews.shape[0]
pros_count = reviews.pros.map(bool).sum()
cons_count = reviews.cons.map(bool).sum()
reviews.stars = reviews.stars.map(lambda stars: float(stars.split("/")[0].replace(",",".")))
average_score = reviews.stars.mean().round(2)
stars = reviews.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value=0).sort_index()
stars.plot.bar(color="gold")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
#plt.show()
plt.savefig(f"plots/{product_id}.png")
plt.close()