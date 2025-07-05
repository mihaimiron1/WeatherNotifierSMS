# WeatherNotifierSMS ☁️📩

A small Python project that checks the weather forecast for your location and sends an SMS notification via Twilio if it will rain — including minimum, maximum, and mid-day temperatures.

## 🌍 Features

- Connects to the OpenWeatherMap API to fetch weather forecasts.
- Detects if it's going to rain in the next hours.
- Calculates and includes min, max, and mid-day temperatures.
- Sends a formatted SMS using Twilio API.
- Can be run locally or hosted on [PythonAnywhere](https://www.pythonanywhere.com/).

## 🛠 Technologies Used

- Python 3
- [OpenWeatherMap API](https://openweathermap.org/forecast5)
- [Twilio SMS API](https://www.twilio.com/docs/sms/send-messages)
- Requests Library

## 📁 Files

- `main.py` – Main local runner.
- `for_pythonanywhere_cod.py` – Optimized script for PythonAnywhere cloud deployment (uses proxy for Twilio).

## 🚀 How to Run

### Local (main.py)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WeatherNotifierSMS.git
   cd WeatherNotifierSMS
   
2. Install dependencies:
  ```bash
     pip install requests twilio
```
3. Replace the following with your credentials:

  - API_KEY from OpenWeatherMap
  - account_sid and auth_token from Twilio
  - Your phone number in to=... and Twilio sender number in from_=...
4. Run:
  ```bash
     python main.py
```

## On PythonAnywhere (for_pythonanywhere_cod.py)
1. Upload the script.

2. Make sure to set the https_proxy environment variable in your PythonAnywhere console:
  ```bash
     export https_proxy=https://your-proxy-address
```
3. Run:
  ```bash
     python3 for_pythonanywhere_cod.py
```

📦 Notes
Ensure you have a Twilio trial account or a paid plan.

The phone numbers must be verified in Twilio if you're using a trial account.

Don't expose your API keys in public repos! Use .env files or environment variables.
