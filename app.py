from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
from PIL import Image
import io
import base64
import cv2
import numpy as np

app = Flask(__name__)

# Load model once at startup
model = YOLO("best.pt")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    img = Image.open(file.stream).convert("RGB")

    # Run inference
    results = model(img)[0]

    # Parse detections
    detections = []
    for box in results.obb:  # OBB boxes
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]
        detections.append({"label": label, "confidence": round(conf, 3)})

    # Render the result image with bounding boxes
    result_img = results.plot()  # numpy array (BGR)
    result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(result_img_rgb)

    # Encode to base64 to send back to frontend
    buffer = io.BytesIO()
    pil_img.save(buffer, format="JPEG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return jsonify({
        "detections": detections,
        "image": f"data:image/jpeg;base64,{encoded}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
