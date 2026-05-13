#!/usr/bin/python3
"""
Task 02 Requests
"""
import requests
import csv

def fetch_and_print_posts():
    """Fetches and prints posts from JSONPlaceholder"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Fetches and saves posts to a CSV file"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        data = [{'id': post.get('id'), 'title': post.get('title'), 'body': post.get('body')} for post in posts]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
