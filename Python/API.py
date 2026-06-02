import json

class WeatherAPI:
    def get_weather(self):
        try:
            response = '''
            {
                "main": {
                    "temp": 31.5
                },
                "weather": [
                    {
                        "description": "scattered clouds"
                    }
                ]
            }
            '''

            data = json.loads(response)

            temperature = data["main"]["temp"]
            condition = data["weather"][0]["description"]

            print("Weather Report")
            print(f"Temperature: {temperature} °C")
            print(f"Condition: {condition}")

        except Exception as e:
            print("Error:", e)

weather = WeatherAPI()
weather.get_weather()