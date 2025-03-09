from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re

HOST = "0.0.0.0"
PORT = 8000

VALID_LETTERS = "АВЕКМНОРСТУХ"
SPECIAL_WORDS = {"ВОР", "ЛОХ", "ССУ", "КОТ", "ДОМ", "РАК", "МИР", "АЧО", "БАС", "БАР", "БЕС", "БИЧ", "БОГ", "БОТ", "БУЛ", 
                 "ГОН", "ГОС", "ГРУ", "ГУД", "ГОК", "АРМ", "ЕКХ", "ХКХ", "МММ", "АМО", "АОО", "ВОО", "МОО", "СОО", "АКР",
                 "ВКР", "СКР", "ЕРЕ", "ММР", "ВМР", "РМР", "АММ", "ККК", "ККХ", "КММ", "КМР", "КОО", "ННН", "ОМР", "МОР",
                 "РМР", "САС", "СММ", "ССС", "ТМР", "УМР"}

def calculate_price(number):
    if not re.match(rf"^[{VALID_LETTERS}]\d{{3}}[{VALID_LETTERS}]{{2}}$", number):
        return "Некорректный формат номера"

    letters = number[0] + number[-2:]
    digits = number[1:4]

    price = 0
    if len(set(digits)) == 1:
        price += 600000
    if len(set(letters)) == 1:
        price += 300000
    if digits in {"001", "002", "003", "004", "005", "006", "007", "008", "009"}:
        price += 500000
    if digits.endswith("00"):
        price += 250000
    if len(set(digits)) == 1 and len(set(letters)) == 1:
        price += 1000000
    if digits[0] == digits[2]:
        price += 70000
    if letters in SPECIAL_WORDS:
        price += 300000

    return price if price > 0 else "Номер не имеет особой ценности"

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/calculate":
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            number = post_data.get("number", "").upper()
            result = calculate_price(number)
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"price": result}).encode())

server = HTTPServer((HOST, PORT), RequestHandler)
server.serve_forever()
