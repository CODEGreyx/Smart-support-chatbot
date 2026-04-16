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
def chat():
    data = request.get_json()
    user_message = data["message"].lower().strip()

    if "open" in user_message or "hours" in user_message or "time" in user_message:
        reply = "We are open Monday to Saturday from 10 AM to 8 PM."

    elif "price" in user_message or "cost" in user_message or "how much" in user_message or "haircut" in user_message or "beard" in user_message:
        reply = "Haircut is €20, beard trim is €10, and haircut plus beard is €25."

    elif "appointment" in user_message or "book" in user_message or "booking" in user_message or "walk in" in user_message:
        reply = "You can walk in, but booking through WhatsApp is recommended."

    elif "location" in user_message or "where" in user_message or "address" in user_message or "located" in user_message:
        reply = "We are located in Berlin near Alexanderplatz."

    elif "services" in user_message or "offer" in user_message:
        reply = "We offer haircuts, beard trims, and haircut plus beard combos."

    elif "hello" in user_message or "hi" in user_message or "hey" in user_message:
        reply = "Hi, welcome. You can ask about opening hours, prices, bookings, location, or services."

    else:
        reply = "Sorry, I did not fully understand that. You can ask about hours, prices, bookings, location, or services."

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run(debug=True)