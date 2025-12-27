from flask import Flask, request

app = Flask(__name__)

mc_queue = []
rb_queue = []

@app.route("/mc", methods=["POST"])
def mc_post():
    mc_queue.append(request.data.decode())
    return "ok"

@app.route("/roblox", methods=["POST"])
def rb_post():
    rb_queue.append(request.data.decode())
    return "ok"

@app.route("/mc", methods=["GET"])
def mc_get():
    if rb_queue:
        return rb_queue.pop(0)
    return ""

@app.route("/roblox", methods=["GET"])
def rb_get():
    if mc_queue:
        return mc_queue.pop(0)
    return ""

app.run(host="0.0.0.0", port=10000)
