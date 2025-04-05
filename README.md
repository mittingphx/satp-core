# SATP Core

SATP Core is a secure memory management system for LLMs, built with a Flask server, encryption utilities, and a memory viewer UI.

## Components

- **Flask Server** (`flask_server/app.py`): Provides endpoints to save, load, and list memory files.
- **Encryption Utility** (`flask_server/encryption.py`): Implements encryption and decryption functions using Fernet.
- **Key Manager** (`flask_server/key_manager.py`): Generates and loads the encryption key.
- **Memory Viewer** (`flask_server/viewer.html`): A simple web UI to view and decrypt saved memories.
- **SATP Memory Store** (`satp_memory_store/`): Directory where encrypted memory files are stored.

## Setup Instructions

1. Clone this repository.
2. Navigate to the `flask_server` directory.
3. Create a Python virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
4.	Install the dependencies:
   ```bash
   pip install flask cryptography
   ```

5. Run the Flask server:
   ```bash
   python app.py
   ```
6.	Open viewer.html in your browser to view and load your memories.

Encryption Details
	•	Memory files are encrypted using Fernet symmetric encryption (AES-based).
	•	The encryption key is generated and stored in satp_memory_store/.satp_key by the key manager.
	•	The Flask server uses this key to encrypt memory upon saving and decrypt it upon loading.

SATP and Future Development

This repository is part of a larger system to enable secure memory management and trust protocols for LLMs. Future updates may include:
	•	Metadata tagging and SATP trust level enforcement
	•	GitHub Actions for automatic deployment and synchronization
	•	Integration with local AI agents for dynamic memory updates



   

---

### **Packaging the Repository**

I've generated a ZIP archive of the repository, which you can now download and inspect.

👉 [Download satp-core.zip](sandbox:/mnt/data/satp-core.zip?_chatgptios_conversationID=67ef82ee-77d4-8005-af50-1d3eaf65c538&_chatgptios_messageID=b89f5a08-3953-4b51-b25a-828defdad23b)

---

### **Next Steps**

1. **Extract and push** the contents of `satp-core.zip` to your GitHub repository at [https://github.com/mittingphx/satp-core](https://github.com/mittingphx/satp-core).
2. **Test locally**:
   - Run the Flask server.
   - Open the viewer in your browser.
   - Save a test memory using a tool like `curl` or Postman.
3. **Further Development**:
   - Implement automated GitHub Actions for continuous deployment.
   - Expand SATP metadata and trust protocols.
   - Integrate a local Cody sync client to automatically pull new memories.

Let me know how it goes or if you need further refinements or next-layer integrations!
