from encryption import generate_key
from pathlib import Path

KEY_FILE = Path("../satp_memory_store/.satp_key")

def save_key():
    key = generate_key()
    KEY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not KEY_FILE.exists():
        return save_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

if __name__ == "__main__":
    key = load_key()
    print("Key loaded:", key.decode())