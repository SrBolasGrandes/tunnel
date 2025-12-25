from flask import Flask, request, jsonify

app = Flask(__name__)

# Cache simples em memória
chunks = {}

@app.route("/")
def home():
    return "MC ↔ Roblox Bridge Online"

@app.route("/uploadChunk", methods=["POST"])
def upload_chunk():
    data = request.json
    key = f"{data['chunkX']}:{data['chunkZ']}"
    chunks[key] = data
    return {"status": "ok"}

@app.route("/getChunk", methods=["GET"])
def get_chunk():
    x = request.args.get("x")
    z = request.args.get("z")
    key = f"{x}:{z}"
    return jsonify(chunks.get(key, {}))

@app.route("/chunks", methods=["GET"])
def all_chunks():
    return jsonify(chunks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
