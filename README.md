# Softlusion

Sentiment analysis and web scraping services. 

## venv

Create virtual environment `virtualenv venv` and activate:

-MacOS and Linux `source venv/bin/activate`.

-Windows `venv\Scripts\activate`.

## Dependencies

Install dependencies `pip install -r requirements.txt`.

## Run

Run `python app.py`.

## Project tree

`tree -L 3`

```
.
├── app.py
├── README.md
├── requirements.txt
├── src
│   ├── sentiment
│   │   ├── __pycache__
│   │   └── sentiment.py
│   └── webscraping
│       ├── __pycache__
│       ├── ws_15mpedia.py
│       └── ws_noticias.py
└── venv
```

## To create requirements.txt

`pipreqs .`.
