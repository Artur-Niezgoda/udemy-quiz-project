"""Module requesting questions for the quiz from opentdb.com - Trivia question database
"""
import requests


AMOUNT = 10 # up to 50
QUESTION_TYPE = "boolean"

response = requests.get(url=f"https://opentdb.com/api.php?amount={AMOUNT}&type={QUESTION_TYPE}")
response.raise_for_status()
question_data = response.json()["results"]
