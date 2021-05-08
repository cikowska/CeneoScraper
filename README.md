# CeneoScraper
## Etap 1 - Pobranie składowych pojedyńczej opinii o konkretnym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
1. Pobranie kodu pojedyńczej strony z opiniami o produkcie
2. Analiza struktury kodu pojedyńczej opinii

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|:-------|:-----------|:-------------|:---------|
|Opinia|`div.js_product-review`|review||
|Identyfikator opinii|review_id|||
|Autor opinii|author|||
|Rekomendacja|`span.user-post__author-recomendation`|recommendation||
|Liczba gwiazdek|`span.user-post__score-count`|stars||
|Treść opinii|`div.user-post__text`|content||
|Lista zalet|`div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item` <br>
`div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item` <br>
`div.review-feature__title--positives ~ div.review-feature__item` <br>|pros||
|Lista wad|`div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item` <br>
`div.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item` <br>
`div.review-feature__title--negatives ~ div.review-feature__item` <br>|cons||
|Dla ilu osób przydatna|`span[id^="votes-yes"]`<br>`button.vote-yes["data-total-vote"]`<br>`button.vote-yes > span`|useful||
|Dla ilu osób nieprzydatna|`span[id^="votes-no"]`<br>`button.vote-no["data-total-vote"]`<br>`button.vote-no > span`|useless||
|Czy potwierdzona zakupem|`div.review-pz`|purchase||
|Data wystawienia opinii|`span.user-post_published > time:nth-child(1)["datetime"]`|review_date||
|Data zakupu produktu|`span.user-post_published > time:nth-child(2)["datetime"]`|purchase_date||