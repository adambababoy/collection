if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")

  def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text
#good
 if OPENWEATHERMAP_API_KEY:
        params_openweathermap = {"q": location, "appid": OPENWEATHERMAP_API_KEY}
        response_openweathermap = requests.get(
            OPENWEATHERMAP_URL_BASE, params=params_openweathermap
        )
        weather_data.append({"OpenWeatherMap": response_openweathermap.json()})
    if WEATHERSTACK_API_KEY:
        params_weatherstack = {"query": location, "access_key": WEATHERSTACK_API_KEY}
        response_weatherstack = requests.get(
            WEATHERSTACK_URL_BASE, params=params_weatherstack#yes
        )
if not weather_data:
        raise ValueError("No API keys provided or no valid data returned.")
    return weather_data


if __name__ == "__main__":
    from pprint import pprint
