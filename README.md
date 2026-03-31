---
title: Cola Pepsi Detection
emoji: 🥤
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
---

# Cola vs Pepsi Detector

A web application that uses a YOLOv8 Oriented Bounding Box (OBB) model to detect and classify **Cola** and **Pepsi** cans/bottles in images. Upload a photo and the app will classify whether the image is Pepsi or Cola.

---

## App Preview

>`![App Preview](preview.png)`

---

## What the Model Does

- Detects **Cola** and **Pepsi** in uploaded images
- Draws **oriented bounding boxes (OBB)** around each detected object
- Returns the **class label** and **confidence score** for each detection
- Built with **YOLOv8m-OBB** from Ultralytics, trained on a custom dataset of ~300 augmented images collected and labeled via Roboflow

## Project Structure

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

## Running Locally with Docker

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

Go to the mentioned url in your browser.

---

## Running Locally without Docker

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the app**
```bash
python app.py
```

**3. Open the app**

Go to your local url and click on it.

---

## How to Use the Interface

1. Open the app in your browser
2. Click **Choose File** and select an image containing a Cola or Pepsi can
3. Click **Detect**
4. The app will display:
   - The image with bounding boxes drawn around detected cans
   - The label (**Cola** or **Pepsi**) and confidence score for each detection

---

## Known Issues & Limitations

- **Small dataset** — the model was trained on ~300 images (augmented from ~50 original images per class), so performance on unusual angles or lighting may vary
- **Two classes only** — the model can only detect Cola and Pepsi cans; other objects will not be detected
- **Corrupt annotations** — a small number of images with bounding box coordinates slightly outside the image boundary were skipped during training, which may slightly affect generalization
---

## Built With

- [YOLOv8](https://github.com/ultralytics/ultralytics) — object detection model
- [Flask](https://flask.palletsprojects.com/) — web framework
- [Roboflow](https://roboflow.com/) — dataset labeling and export
- [Albumentations](https://albumentations.ai/) — data augmentation
- [Docker](https://www.docker.com/) — containerization

---

##  Author

**Mahra AlHarmoodi**
