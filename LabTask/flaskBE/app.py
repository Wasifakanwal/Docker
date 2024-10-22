from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://myuser:mypassword@db:5432/mydb"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == "__main__":
    app.run()