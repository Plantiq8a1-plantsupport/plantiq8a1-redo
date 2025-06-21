# IoT.py --- IoT (using API to get GPS - IoT works without an API but only on the web - Javascript!)
import urllib.request
import json

#Location -- write here 
lat = 
lon = 

#API KEY
api_key = "IOT_API_KEY"  

_thong_tin_prompt = ""

def _lay_thoi_tiet():
    global _thong_tin_prompt
    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=vi"
        )
        with urllib.request.urlopen(url) as response:
            raw = response.read()
            result = json.loads(raw)
            nhiet_do = result["main"]["temp"]
            do_am = result["main"]["humidity"]
            thoi_tiet = result["weather"][0]["description"]
            vi_tri = result.get("name", "khu vực của bạn")

            _thong_tin_prompt = (
                f"\nHiện tại tại {vi_tri}, thời tiết là {thoi_tiet}, "
                f"nhiệt độ {nhiet_do}°C, độ ẩm {do_am}%. 📍(lat: {lat}, lon: {lon})"
            )
    except Exception as e:
        _thong_tin_prompt = f"\n(Không thể lấy dữ liệu IoT: {e})"


_lay_thoi_tiet()

def get_prompt():
    return _thong_tin_prompt
