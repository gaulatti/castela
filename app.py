from flask import Flask, request, render_template
from transformers import pipeline
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

generator = pipeline('summarization', model='facebook/bart-large-cnn')

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/', methods=['POST'])
def generate_text():
    url = request.form['url']
    website_text = scrape_website(url)
    summary = generator(website_text, max_length=130, min_length=30, do_sample=False)
    return render_template('index.html', url=url, output=summary[0]['summary_text'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
