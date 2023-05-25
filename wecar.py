import requests
import time
import json
import csv

API_KEY = 'AIzaSyAveu3EDXNBYRB2RxG7YC27GZGv07wFjQg'
SEARCH_ENGINE_ID = '83889be6051554daa'
QUERY = 'site:youtube.com openinapp.co'
RESULTS_PER_REQUEST = 10
TOTAL_RESULTS = 10000

def scrape_youtube_links():
    results = []
    start = 1

    while start <= TOTAL_RESULTS:
        url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={QUERY}&start={start}&num={RESULTS_PER_REQUEST}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            results.extend([item['link'] for item in items])

            start += RESULTS_PER_REQUEST
            time.sleep(2)  # Delay between requests to avoid rate limit

        else:
            print(f'Error: {response.status_code}')
            break

    youtube_links = [link for link in results if "youtube.com" in link]
    return youtube_links

# Scrape YouTube links
youtube_links = scrape_youtube_links()

# Save results to JSON
with open('youtube_links.json', 'w') as json_file:
    json.dump(youtube_links, json_file, indent=4)

# Save results to CSV
with open('youtube_links.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['YouTube Links'])
    writer.writerows([[link] for link in youtube_links])
