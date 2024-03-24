from flask import Flask, request, jsonify
from flask_cors import CORS
'''from Text_summarization import Summarization'''
from chat_with_document import VectorizationPDF, ChatDocument  # Updated import
import os

app = Flask(__name__)
CORS(app)

@app.route("/members", methods=['GET'])
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

'''@app.route("/summarize", methods=['POST'])
def summarize():
    data = request.get_json()
    para = data.get('para')
    return jsonify({"response": Summarization(para)})  # return the summarize function here.'''

@app.route("/docchat", methods=['POST'])
def document_chat():
    data = request.get_json()
    message = data.get('text')
    pdf_path = data.get('pdf_path')  # Updated variable name
    if not os.path.exists(pdf_path):
        return jsonify({"error": f"File not found: {pdf_path}"}), 404
    conversation = VectorizationPDF(pdf_path)  # Updated function call
    response = ChatDocument(conversation, message)  # Updated function call
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
