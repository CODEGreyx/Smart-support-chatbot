from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

INSTAGRAM_PROMPTS = [
    {
        "id": 1,
        "title": "Viral Content Ideas",
        "category": "Strategy",
        "prompt": (
            "You are a social media strategist specialized in rapid growth. "
            "Analyze the latest 10 viral Instagram trends in web development, "
            "building websites with AI, and tech tools for creators and entrepreneurs. "
            "Create 5 short, explosive content ideas with high share potential "
            "for an audience of developers, freelancers, and tech-savvy founders. "
            "Be specific and practical."
        )
    },
    {
        "id": 2,
        "title": "Pain Point Hooks",
        "category": "Hooks",
        "prompt": (
            "List the 10 biggest pain points that beginner and intermediate developers, "
            "freelancers, and tech entrepreneurs feel about building websites and web apps. "
            "Turn each pain point into a hook of up to 10 words, "
            "ready to be used in Reels. Avoid clichés, be direct and provocative."
        )
    },
    {
        "id": 3,
        "title": "Reels Script (30 sec)",
        "category": "Scripts",
        "prompt": (
            "Create a 30-second script for an Instagram Reel about [choose a topic: "
            "e.g. building a landing page in 1 hour, AI tools for developers, "
            "the fastest way to launch a website]. "
            "Structure: 1) Irresistible hook, 2) Short engaging story, "
            "3) CTA to comment or save. Use short and simple sentences. No fluff."
        )
    },
    {
        "id": 4,
        "title": "Social Proof Phrases",
        "category": "Social Proof",
        "prompt": (
            "Take this result: [insert your result — e.g. 'I built a full website "
            "in 2 hours using AI', 'I got my first freelance client in 30 days', "
            "'I automated my entire workflow with no code'] and create 5 short phrases "
            "that communicate social proof and curiosity, perfect for on-screen text "
            "in videos. Keep maximum impact in up to 10 words."
        )
    },
    {
        "id": 5,
        "title": "Save-Worthy Tips",
        "category": "Carousels",
        "prompt": (
            "List 5 practical and little-known tips about building websites and web apps "
            "faster using AI and modern tools. "
            "Each tip must be a maximum of 12 words, clear and easy to apply. "
            "The goal is to create a carousel that developers and founders can't help but save."
        )
    },
    {
        "id": 6,
        "title": "Repurpose Content",
        "category": "Repurposing",
        "prompt": (
            "Turn this text [paste your web/tech content here] into: "
            "1. a 7-second Reels script with a punchy hook for a tech audience, "
            "2. a 5-slide carousel breaking it into actionable steps, "
            "3. a static post with a single powerful statement developers will screenshot. "
            "Adapt the language and format for each one."
        )
    },
    {
        "id": 7,
        "title": "Irresistible CTAs",
        "category": "CTAs",
        "prompt": (
            "Create 10 short, creative, and direct CTAs that encourage comments "
            "or saves on posts about web development, building with AI, and tech tools. "
            "Target audience: developers, freelancers, and tech entrepreneurs. "
            "Avoid generic phrases, use curiosity triggers and immediate action."
        )
    }
]


@app.route("/")
def home():
    return send_file("index.html")


@app.route("/about")
def about():
    return "This is my about page"


@app.route("/prompts", methods=["GET"])
def get_prompts():
    return jsonify({"prompts": INSTAGRAM_PROMPTS})


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

    elif match(["instagram", "prompt", "viral", "reels", "reel", "hook",
                "carousel", "cta", "content", "followers", "social media", "growth"]):
        reply = (
            "Check out the Instagram Prompts tab for 7 proven prompts "
            "to grow your account — covering viral ideas, hooks, Reels scripts, "
            "social proof, carousels, content repurposing, and CTAs."
        )

    elif match(["hello", "hi", "hey", "yo"]):
        reply = (
            "Hi, welcome! Ask about our opening hours, prices, bookings, "
            "location, or services. You can also check the Instagram Prompts "
            "tab for content creation tools."
        )

    else:
        reply = (
            "Sorry, I don't understand that. You can ask about opening hours, "
            "prices, bookings, location, or services — or explore the "
            "Instagram Prompts tab."
        )

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
