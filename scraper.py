import requests
from bs4 import BeautifulSoup

response =requests.get("https://www.ceneo.pl/99756635#tag=nph_row_promotion")
#print(response.status_code)
#print(response.text)

page_dom = BeautifulSoup(response.text, "html.parser")

'''reviews = page_dom.select("div.js_product-review")
print(type(reviews))
review = reviews.pop(0)
print(type(review))'''
review = page_dom.select_one("div.js_product-review")
print(type(review))

review_id = review["data-entry-id"]

author = review.select_one("span.user-post__author-name").text.strip()

recommendation = review.select_one("span.user-post__author-recomendation").text.strip()

#recommendation = review.select_one("span.user-post__author-recomendation > em").string.strip()
stars = review.select_one("span.user-post__score-count").text.strip()

content = review.select_one("div.user-post__text").text.strip()

pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
#print(pros.pop(0).text.strip())

cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")

useful = review.select_one("button.vote-yes > span").text.strip()

useless = review.select_one("button.vote-no > span").text.strip()

purchase = review.select_one("div.review-pz").text.strip()

review_date = review.select_one("span.user-post__published > time:nth-child(1)")["datetime"]

purchase_date = review.select_one("span.user-post__published > time:nth-child(2)")["datetime"]

print(purchase_date)
exit()

