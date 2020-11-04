# Google Search Engine Result Scrapper - Python

Scrapes prepared search terms from a google search and saves it to a csv file.

Run it manually or schedule it daily to track search results over time.

### Installation

- clone this repo in a project folder
- make a virtual environment
- install the requiremd modules
- prepare search terms in txt files in "search_lists" folder (see example files)
- run script
- results will be saved as a csv file per search term.

```
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scrape.py
```

### Notes

- you can have multiple txt files in the **search_lists** folder
- One search term per line (no commas required)
- You can change the **no_of_pages** results in **scrape.py**
- You may need to tweak requests **header** in **scrape.py** for better results
- Script doesn't seem to like search terms that are too broad.
- Running the script multiple times will append the results to same file
- ^ is used as the csv delimiter, You can split the text to columns in your favorite spreadsheet.