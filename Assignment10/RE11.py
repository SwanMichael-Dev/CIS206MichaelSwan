import re

def extract_date_from_url(url):
    match = re.search(r'(\d{4})/(\d{2})/(\d{2})', url)
    if match:
        year, month, day = match.groups()
        return year, month, day
    else:
        return None, None, None

url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
year, month, day = extract_date_from_url(url)
print(f"Year: {year}, Month: {month}, Day: {day}")
