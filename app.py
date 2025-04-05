from flask import Flask, request, jsonify
import os
import hashlib
from encryption import encrypt_data, decrypt_data
from key_manager import load_key

app = Flask(__name__)
MEMORY_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../satp_memory_store")
ENCRYPTION_KEY = load_key()

@app.route("/save-memory", methods=["POST"])
def save_memory():
    data = request.json
    title = data.get("title", "untitled").replace(" ", "_")
    content = data.get("content", "")
    encrypted_content = encrypt_data(content, ENCRYPTION_KEY)
    satp_hash = hashlib.sha256(encrypted_content.encode()).hexdigest()
    filename = f"{title}_{satp_hash[:8]}.md"
    filepath = os.path.join(MEMORY_DIR, filename)
    os.makedirs(MEMORY_DIR, exist_ok=True)
    with open(filepath, "w") as f:
        f.write(encrypted_content)
    return jsonify({"status": "saved", "file": filename})

@app.route("/load-memory", methods=["POST"])
def load_memory():
    data = request.json
    filename = data.get("filename")
    filepath = os.path.join(MEMORY_DIR, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "file not found"}), 404
    with open(filepath, "r") as f:
        encrypted = f.read()
    try:
        decrypted = decrypt_data(encrypted, ENCRYPTION_KEY)
        return jsonify({"content": decrypted})
    except Exception as e:
        return jsonify({"error": "decryption failed", "details": str(e)}), 500

@app.route("/list-memories", methods=["GET"])
def list_memories():
    if not os.path.exists(MEMORY_DIR):
        return jsonify([])
    files = os.listdir(MEMORY_DIR)
    return jsonify([f for f in files if f.endswith(".md")])

@app.route("/satp-check", methods=["POST"])
def satp_check():
    # Stub: Always returns trust_level 2 for now
    return jsonify({"trust_level": 2, "ok_to_store": True})

if __name__ == "__main__":
    app.run(port=5000)