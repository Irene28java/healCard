from flask import Blueprint, render_template, redirect, request, session, url_for
from .wallet import add_card, list_cards, simulate_payment
from .models import Card, db
from .user import User
from .vpn import connect_vpn, disconnect_vpn

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("main.login"))
    cards = Card.query.all()
    return render_template("dashboard.html", cards=cards)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            return redirect(url_for("main.home"))
        return "Credenciales Incorrectas", 401
    return render_template("login.html")

@bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("main.login"))

@bp.route("/vpn/<int:card_id>/toggle")
def toggle_vpn(card_id):
    card = Card.query.get(card_id)
    card.vpn_enabled = not card.vpn_enabled
    db.session.commit()
    if card.vpn_enabled:
        connect_vpn(card_id)
    else:
        disconnect_vpn(card_id)
    return redirect(url_for("main.home"))


#Cuando el Usuario añade una tarjeta 
add_card(user_id=session["user_id"], card_number="4111111111111", name_on_card="Carlos A.", expiry="12/30")

#Para Mostrar en el Dashboard
cards = list_cards(session["user_id"])

# Para simular Pago
mensaje = simulate_payment(session["user_id"], amount=20)