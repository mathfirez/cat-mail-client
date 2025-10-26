import httpx
import json

def get_last_message() -> tuple[str, str, str]:
    with open('catmailclient.json') as f:
        catmail_cfg = json.load(f)

    authorization = catmail_cfg['AUTHORIZATION']
    server = catmail_cfg['SERVER']

    r = httpx.get(server, headers={"Authorization": authorization})
    status_code = r.status_code
    if status_code == 200:
        dataJson = r.json()
        msg_str = dataJson.get("Content")
        author_str = dataJson.get("Author")
        posted_on_str = dataJson.get("PostedOn")

        return msg_str, author_str, posted_on_str
    return "", "", ""
