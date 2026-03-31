# 🥤 Cola vs Pepsi Detector

A web application that uses a YOLOv8 Oriented Bounding Box (OBB) model to detect and classify **Cola** and **Pepsi** cans in images. Upload a photo and the app will draw bounding boxes around any cans it finds and tell you what it detected.

---

## 📸 App Preview

> _Add a screenshot or GIF of your app here after you take one._
> _You can replace this line with:_ `![App Preview](preview.png)`

---

## 🧠 What the Model Does

- Detects **Cola** and **Pepsi** cans in uploaded images
- Draws **oriented bounding boxes (OBB)** around each detected object
- Returns the **class label** and **confidence score** for each detection
- Built with **YOLOv8m-OBB** from Ultralytics, trained on a custom dataset of ~300 augmented images collected and labeled via Roboflow

**Model Performance (Test Set):**
| Metric | Score |
|--------|-------|
| mAP50 | 0.962 |
| mAP50-95 | 0.865 |
| Cola Recall | 0.993 |
| Pepsi Precision | 0.976 |

---

## 🗂️ Project Structure

```
model_deployment/
├── app.py                  # Main Flask application
├── best.pt                 # Trained YOLOv8 model weights
├── Dockerfile              # Docker container configuration
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Frontend interface
```

---

## 🚀 Running Locally with Docker

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/mahra-alh/cola-pepsi-detector.git
cd cola-pepsi-detector
```

**2. Build the Docker image**
```bash
docker build -t cola-pepsi-detector .
```

**3. Run the container**
```bash
docker run -p 5000:5000 cola-pepsi-detector
```

**4. Open the app**

Go to `http://127.0.0.1:5000` in your browser.

---

## 🖥️ Running Locally without Docker

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the app**
```bash
python app.py
```

**3. Open the app**

Go to `http://127.0.0.1:5000` in your browser.

---

## 📖 How to Use the Interface

1. Open the app in your browser
2. Click **Choose File** and select an image containing a Cola or Pepsi can
3. Click **Detect**
4. The app will display:
   - The image with bounding boxes drawn around detected cans
   - The label (**Cola** or **Pepsi**) and confidence score for each detection

---

## ⚠️ Known Issues & Limitations

- **Small dataset** — the model was trained on ~300 images (augmented from ~50 original images per class), so performance on unusual angles or lighting may vary
- **Two classes only** — the model can only detect Cola and Pepsi cans; other objects will not be detected
- **Corrupt annotations** — a small number of images with bounding box coordinates slightly outside the image boundary were skipped during training, which may slightly affect generalization
- **Imbalanced splits** — augmentation was only applied to the training set, leaving validation and test sets small (19 images each), so evaluation metrics may shift with a single wrong prediction
- **Development server** — the app runs on Flask's built-in development server, which is not suitable for high-traffic production use

---

## 🛠️ Built With

- [YOLOv8](https://github.com/ultralytics/ultralytics) — object detection model
- [Flask](https://flask.palletsprojects.com/) — web framework
- [Roboflow](https://roboflow.com/) — dataset labeling and export
- [Albumentations](https://albumentations.ai/) — data augmentation
- [Docker](https://www.docker.com/) — containerization

---

## 👩‍💻 Author

**Mahra AlHarmoodi** — S2026_162
