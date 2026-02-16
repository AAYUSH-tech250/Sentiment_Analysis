from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sentiment Analyzer</title>
    <style>
        * {
            box-sizing: border-box;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card {
            background: #ffffff;
            width: 420px;
            padding: 30px;
            border-radius: 14px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            text-align: center;
        }

        h1 {
            margin-bottom: 10px;
            color: #333;
        }

        p {
            color: #666;
            font-size: 14px;
            margin-bottom: 20px;
        }

        textarea {
            width: 100%;
            height: 120px;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #ccc;
            resize: none;
            font-size: 14px;
            outline: none;
        }

        textarea:focus {
            border-color: #667eea;
            box-shadow: 0 0 6px rgba(102,126,234,0.5);
        }

        button {
            width: 100%;
            margin-top: 18px;
            padding: 12px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        .footer {
            margin-top: 15px;
            font-size: 12px;
            color: #999;
        }
    </style>
</head>
<body>

    <div class="card">
        <h1>Sentiment Analyzer</h1>
        <p>Analyze emotions in your text instantly</p>

        <form action="/predict" method="post">
            <textarea name="text" placeholder="Enter your text here..." required></textarea>
            <button type="submit">Analyze Sentiment</button>
        </form>

        <div class="footer">
            Powered by FastAPI & ML
        </div>
    </div>

</body>
</html>
"""


@app.post("/predict", response_class=HTMLResponse)
def predict(text: str = Form(...)):
    # Dummy prediction (replace with ML model)
    sentiment = "Positive 😊" if (
            "happy" in text.lower() or
            "good" in text.lower() or
            "great" in text.lower() or
            "awesome" in text.lower()
    ) else "Negative 😞"
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
    <style>
        body {{
            height: 100vh;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial;
        }}
        .result {{
            background: white;
            padding: 30px;
            border-radius: 14px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            width: 400px;
        }}
        h2 {{
            color: #333;
        }}
        a {{
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            color: white;
            background: #667eea;
            padding: 10px 20px;
            border-radius: 8px;
        }}
    </style>
</head>
<body>

    <div class="result">
        <h2>Sentiment Result</h2>
        <p><strong>{sentiment}</strong></p>
        <a href="/">Analyze Another</a>
    </div>

</body>
</html>
"""