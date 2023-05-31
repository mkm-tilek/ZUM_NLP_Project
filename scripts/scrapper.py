!pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

import snscrape.modules.twitter as sntwitter
import csv
import os

folder_path = os.path.join(os.getcwd(), '/content/drive/MyDrive/ZUM/Project/Assignment 1/data')

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

limit = 200000
split_size = 10000
split_count = 1

output_path = os.path.join(folder_path, "tweets")
scraped_tweets = 0

while scraped_tweets < limit:
    output = f"{output_path}_{split_count}.csv"
    with open(output, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Author", "Tweet Text", "Hashtags"])

        for i, tweet in enumerate(sntwitter.TwitterSearchScraper("war since:2020-01-01 until:2023-03-01").get_items()):
            if i >= split_size:
                break
            writer.writerow([tweet.username, tweet.content, tweet.hashtags])
            scraped_tweets += 1

print(f"Scraped {scraped_tweets} tweets.")


