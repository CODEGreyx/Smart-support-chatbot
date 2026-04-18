from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/about")
def about():
    return "This is my about page"

@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"].lower().strip()

    def match(words):
        return any(word in user_message for word in words)

    if match(["open", "hours", "time", "today", "tomorrow", "sunday"]):
        reply = "We are open Monday to Saturday from 10 AM to 8 PM."

    elif match(["price", "cost", "how much", "haircut", "beard", "fade", "trim"]):
        reply = "Haircut is €20, beard trim is €10, and haircut plus beard is €25."

    elif match(["appointment", "book", "booking", "reserve", "walk in"]):
        reply = "You can walk in, but booking through WhatsApp is recommended."

    elif match(["number", "phone", "contact", "whatsapp"]):
        reply = "You can contact us on Whatsapp at +49 123 456789."

    elif match(["location", "where", "address", "near", "located"]):
        reply = "We are located in Berlin near Alexanderplatz."

    elif match(["services", "offer", "do you do"]):
        reply = "We offer haircuts, beard trims and haircut plus beard combos."

    elif match(["hello", "hi", "hey", "yo"]):
        reply = "Hi, welcome. You can ask about opening hours, prices, bookings, location, or services."

    else:
        reply = "Sorry, I dont understand that. You can ask about opening hours, prices, bookings, location, or services."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
