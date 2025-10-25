import httpx

def get_last_message() -> str:
    r = httpx.get("http://localhost:8000/message", headers={"Authorization": "5f857d80-886c-4205-85da-1b52a029d4db"})
    return r.json().get("Content")
