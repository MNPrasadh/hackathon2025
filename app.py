import os
import cv2
import re
import validators
from flask import Flask, render_template, request, redirect, url_for, flash
from PIL import Image
import pytesseract

# Set the Tesseract-OCR path manually
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used for flashing messages

# Function to extract links from text
def extract_links(text):
    url_pattern = r"(https?://[^\s]+)"
    links = re.findall(url_pattern, text)
    return links

# Function to check if the link is suspicious
def is_suspicious(link):
    suspicious_keywords = ["free", "click", "verify", "login", "bank", "update", "password"]
    return any(keyword in link.lower() for keyword in suspicious_keywords)

UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part", "danger")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("No selected file", "danger")
            return redirect(request.url)

        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # Load image and extract text
            image = Image.open(file_path)
            image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
            extracted_text = pytesseract.image_to_string(image)

            # Extract and check links
            links_found = extract_links(extracted_text)
            suspicious_links = [link for link in links_found if is_suspicious(link)]

            return render_template("index.html", image=file.filename, text=extracted_text, links=links_found, suspicious_links=suspicious_links)

    return render_template("index.html", image=None, text=None, links=None, suspicious_links=None)

if __name__ == "__main__":
    app.run(debug=True)
