from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# small local fallback facts (key = "month/day")
FALLBACK_FACTS = {
    "1/1": "January 1 — New Year's Day is celebrated worldwide.",
    "1/26": "January 26 — India celebrates Republic Day.",
    "2/14": "February 14 — Valentine's Day is celebrated in many countries.",
    "3/8": "March 8 — International Women's Day is observed globally.",
    "3/15": "March 15 — Julius Caesar was assassinated on the Ides of March.",
    "4/22": "April 22 — Earth Day is celebrated around the world.",
    "4/30": "April 30 — Vietnam War ended in 1975 with the fall of Saigon.",
    "5/23": "May 23 — Many cultural and historical events took place on this day.",
    "6/5": "June 5 — World Environment Day is celebrated.",
    "6/8": "June 8 — World Oceans Day is observed globally.",
    "7/4": "July 4 — United States celebrates Independence Day.",
    "8/15": "August 15 — India celebrates Independence Day.",
    "9/5": "September 5 — Teachers' Day is celebrated in India.",
    "9/11": "September 11 — The 9/11 attacks occurred in the United States in 2001.",
    "10/31": "October 31 — Halloween is celebrated in many countries.",
    "11/11": "November 11 — World War I ended on Armistice Day in 1918.",
    "12/25": "December 25 — Christmas Day is celebrated around the world."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fact', methods=['POST'])
def fact():
    month = request.form.get('month', '').strip()
    day = request.form.get('day', '').strip()

    # basic validation
    if not month.isdigit() or not day.isdigit():
        return render_template('result.html', fact="Invalid date. Please provide numeric month and day.", source="local")

    month_num = int(month)
    day_num = int(day)
    key = f"{month_num}/{day_num}"

    url = f"http://numbersapi.com/{month_num}/{day_num}/date"

    try:
        # set a timeout so the request doesn't hang forever
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        fact_text = res.text
        source = "numbersapi"
    except requests.exceptions.RequestException:
        # network error, timeout, DNS failure, etc. -> use fallback
        fact_text = FALLBACK_FACTS.get(key, "Sorry — couldn't fetch a fact for that date right now. Try again later.")
        source = "local/fallback"

    return render_template('result.html', fact=fact_text, source=source, month=month_num, day=day_num)

if __name__ == "__main__":
    app.run(debug=True)
