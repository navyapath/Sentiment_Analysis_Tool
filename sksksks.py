from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Sentiment Analysis with Flask</title>
  <style>
      body {
          font-family: Arial, sans-serif;
          background: #f5f5f5;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
          margin: 0;
      }
      .container {
          background: white;
          padding: 2rem;
          border-radius: 8px;
          box-shadow: 0 6px 12px rgba(0,0,0,0.1);
          max-width: 400px;
          width: 100%;
      }
      h1 {
          margin-bottom: 1rem;
          color: #333;
          text-align: center;
      }
      textarea {
          width: 100%;
          height: 100px;
          padding: 0.5rem;
          font-size: 1rem;
          border: 1px solid #ccc;
          border-radius: 4px;
          resize: vertical;
          margin-bottom: 1rem;
      }
      button {
          width: 100%;
          background-color: #4CAF50;
          color: white;
          border: none;
          padding: 0.75rem;
          font-size: 1rem;
          border-radius: 4px;
          cursor: pointer;
      }
      button:hover {
          background-color: #45a049;
      }
      .result {
          margin-top: 1rem;
          font-weight: bold;
          text-align: center;
          color: #2c3e50;
      }
  </style>
</head>
<body>
  <div class="container">
    <h1>Sentiment Analysis</h1>
    <form method="POST" action="/">
      <textarea name="text" placeholder="Enter your sentence here..." required>{{ text }}</textarea>
      <button type="submit">Analyze Sentiment</button>
    </form>
    {% if sentiment %}
    <div class="result">
      Sentiment: <span>{{ sentiment }}</span>
    </div>
    {% endif %}
  </div>
</body>
</html>
'''

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    text = ''
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
    return render_template_string(HTML_TEMPLATE, sentiment=sentiment, text=text)

if __name__ == '__main__':
    app.run(debug=True)
