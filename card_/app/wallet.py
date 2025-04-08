import base64
from cryptography.fernet import Fernet

#Genera Una Clave Segura ( Puedes Guardar esta en tu .env o settings)

key = Fernet.generaate_key
cipher = Fernet(key)

wallet_cards = {}

def add_card(user_id, card_number, name_on_card, expiry):
    encrypted_card = cipher.encrypt(card_number.encode())
    card = {
        "number" : encrypted_card,
        "name" : name_on_card,
        "expiry" : expiry
              
               
                 }
    if user_id not in wallet_cards:
        wallet_cards[user_id] = []
        wallet_cards[user_id].append(card)
        return True
    
    def list_cards(user_id):
        cards = wallet_cards.get(user_id, [])
        return [
            {
                "number": cipher.decrypt(card["number"]).decode(),
                "name": card["name"]
                "expiry": card["expiry"]
            }
        for card in cards
        ]
def simulate_payment(user_id, amount):
    cards = wallet_cards.get(user_id, [])
    if not cards:
        return "No hay tarjetas registradas"
    
    #Simulacion el uso de la primera tarjeta

    selected = cards[0]
    return f"pago de {amount}€ realizado con la tarjeta terminada en {cipher.decrypt(selected['number']).decode()[-4:]}"
