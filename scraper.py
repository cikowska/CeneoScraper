import requests

respons =requests.get("https://www.ceneo.pl/99756635#tag=nph_row_promotion")

#print(respons.status_code)
print(respons.text)