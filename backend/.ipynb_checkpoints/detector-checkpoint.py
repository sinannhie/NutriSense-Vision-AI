from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def detect_food(image_path):

    results = model(image_path)

    detected_items = []

    for result in results:

        for box in result.boxes:

            confidence = float(box.conf[0])

            if confidence < 0.5:
                continue

            cls = int(box.cls[0])

            name = model.names[cls]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detected_items.append({
                "name": name,
                "confidence": round(confidence, 2),
                "bbox": [x1, y1, x2, y2]
            })

    return detected_items