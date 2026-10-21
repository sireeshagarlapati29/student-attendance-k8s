
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Student Attendance System is running!"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/attendance")
def attendance():
    return jsonify({
        "student": "Student1",
        "attendance": "Present"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)