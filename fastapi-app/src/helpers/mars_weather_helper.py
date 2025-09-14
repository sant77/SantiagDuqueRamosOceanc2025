
class MarsWeatherHelper:
    @staticmethod
    def format_weather_data(data):
        formatted_data = {
            "temperature": data.get("temperature"),
            "atmospheric_pressure": data.get("pressure"),
            "wind_speed": data.get("wind_speed"),
            "weather_condition": data.get("condition"),
        }
        return formatted_data