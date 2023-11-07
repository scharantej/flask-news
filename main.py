 
# Import the necessary modules
from flask import Flask, render_template, request
import requests

# Create a Flask app
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    # Render the home page template
    return render_template('home.html')

# Define the news route
@app.route('/news')
def news():
    # Get the news articles from the API
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY')
    articles = response.json()['articles']

    # Render the news page template
    return render_template('news.html', articles=articles)

# Define the article route
@app.route('/article/<int:article_id>')
def article(article_id):
    # Get the article from the API
    response = requests.get('https://newsapi.org/v2/articles?id={}&apiKey=YOUR_API_KEY'.format(article_id))
    article = response.json()

    # Render the article page template
    return render_template('article.html', article=article)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


HTML code for home.html

html
<!DOCTYPE html>
<html>
<head>
  <title>News App</title>
</head>
<body>
  <h1>News App</h1>
  <a href="/news">See the news</a>
</body>
</html>


HTML code for news.html

html
<!DOCTYPE html>
<html>
<head>
  <title>News App</title>
</head>
<body>
  <h1>News</h1>
  <ul>
    {% for article in articles %}
      <li><a href="/article/{{ article['id'] }}">{{ article['title'] }}</a></li>
    {% endfor %}
  </ul>
</body>
</html>


HTML code for article.html

html
<!DOCTYPE html>
<html>
<head>
  <title>News App</title>
</head>
<body>
  <h1>{{ article['title'] }}</h1>
  <p>{{ article['content'] }}</p>
</body>
</html>
