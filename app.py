from flask import Flask, request

app = Flask(__name__)

mc_to_rb = ""
rb_to_mc = ""

@app.route("/mc", methods=["POST"])
def mc_chat():
    global mc_to_rb
    mc_to_rb = request.data.decode()
    return "ok"

@app.route("/roblox", methods=["POST"])
def rb_chat():
    global rb_to_mc
    rb_to_mc = request.data.decode()
    return "ok"

@app.route("/mc", methods=["GET"])
def get_mc():
    global rb_to_mc
    msg = rb_to_mc
    rb_to_mc = ""
    return msg

@app.route("/roblox", methods=["GET"])
def get_rb():
    global mc_to_rb
    msg = mc_to_rb
    mc_to_rb = ""
    return msg

app.run(host="0.0.0.0", port=10000)
