from flask import Flask, render_template, request, flash
from weather import WeatherFetcher

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if city:
            weather_fetcher = WeatherFetcher()
            weather_data = weather_fetcher.fetch_weather(city)
            if not weather_data:
                flash('City not found or there was an error fetching weather data. Please try again.', 'danger')
    
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
