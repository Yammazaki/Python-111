BOT_API_TOKEN = '5522039050:AAExrISV_tFC0qVDZThsIn_clRYc5kv-q10'
WEATHER_API_KEY = '29253d203213a557b461efe5fa8b47f6'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)