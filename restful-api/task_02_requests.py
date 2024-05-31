#!/usr/bin/python3
''' module documentation '''
import requests
import csv


def fetch_and_print_posts():
    '''
    does what it says on the tin
    '''
    url = "https://jsonplaceholder.typicode.com/posts"
    good_status_codes = [200]
    response = requests.get(url)
    if response.status_code in good_status_codes:
        print("Status Code: {}".format(response.status_code))
        list_posts = response.json()
        for post in list_posts:
            print(post["title"])

def fetch_and_save_posts():
    '''
    does what it says on the tin
    '''
    url = "https://jsonplaceholder.typicode.com/posts"
    good_status_codes = [200]
    csv_file = "posts.csv"
    fieldnames = ["id", "title", "body"]
    response = requests.get(url)
    if response.status_code in good_status_codes:
        list_posts = response.json()
        with open(csv_file, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames, extrasaction='ignore')
            writer.writeheader()
            for post in list_posts:
                writer.writerow(post)