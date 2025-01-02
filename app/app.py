from flask import Flask, render_template, request, jsonify
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from PyPDF2 import PdfReader
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the model and tokenizer
MODEL_DIR = "./deployment_model"
tokenizer = PegasusTokenizer.from_pretrained(MODEL_DIR)
model = PegasusForConditionalGeneration.from_pretrained(MODEL_DIR)

# Summarization function
def summarize_text(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=128, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint: Summarize Text
@app.route('/summarize/text', methods=['POST'])
def summarize_from_text():
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    summary = summarize_text(text)
    return jsonify({"summary": summary})

# API endpoint: Summarize PDF
@app.route('/summarize/pdf', methods=['POST'])
def summarize_from_pdf():
    pdf_file = request.files.get("file")
    if not pdf_file:
        return jsonify({"error": "No PDF file provided"}), 400

    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    summary = summarize_text(text)
    return jsonify({"summary": summary})

# API endpoint: Summarize URL
@app.route('/summarize/url', methods=['POST'])
def summarize_from_url():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join([para.get_text() for para in paragraphs])
    summary = summarize_text(text)
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)