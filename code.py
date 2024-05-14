from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

def generate_random_temperature():
    return round(random.uniform(25, 30), 2)

def generate_random_humidity():
    return round(random.uniform(35, 70), 2)

@app.get("/", response_class=HTMLResponse)
async def read_data():
    temperature = generate_random_temperature()
    humidity = generate_random_humidity()
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Temperature and Humidity Data</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    text-align: center;
                    color: #333;
                }}
                #data-container {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                p {{
                    margin: 10px 0;
                    font-size: 1.2em;
                }}
                button {{
                    display: block;
                    margin: 0 auto;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }}
                button:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Temperature and Humidity Data</h1>
                <div id="data-container">
                    <p><i class="fas fa-cloud"></i> Thai Nguyen</p>
                    <p id="temperature"><i class="fas fa-thermometer-half"></i> Temperature: <span id="temp-value">{temp}</span> °C</p>
                    <p id="humidity"><i class="fas fa-tint"></i> Humidity: <span id="humidity-value">{humidity}</span> %</p>
                </div>
                <button onclick="refreshData()">Refresh Data</button>
            </div>

            <script>
                function refreshData() {{
                    fetch('/')
                    .then(response => response.json())
                    .then(data => {{
                        document.getElementById('temp-value').innerText = data.temperature;
                        document.getElementById('humidity-value').innerText = data.humidity;
                    }});
                }}

                refreshData(); // Load initial data when page loads
            </script>
        </body>
        </html>
    """.format(temp=temperature, humidity=humidity)
