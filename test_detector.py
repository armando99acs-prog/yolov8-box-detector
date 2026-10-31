import cv2
from ultralytics import YOLO
import os

# Se defina BASE_DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Se carga el modelo
model_path = os.path.join(BASE_DIR, "mis_resultados", "Yolov8m", "weights", "best.pt")
model = YOLO(model_path)

# Se abre el video (0 para webcam)
video_path = os.path.join(BASE_DIR, "video_prueba.mp4")
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Fin del video o no se pudo acceder a la fuente.")
        break

    # Se analiza el video cada frame
    results = model(frame, conf=0.5)  # 50% de confianza mínima

    # Señala cada caja dentro de un cuadro
    annotated_frame = results[0].plot()

    # Muestra el video analizado en tiempo real
    cv2.imshow("Sistema de Inspeccion Logistica - IA", annotated_frame)

    # Para abortar el analisis del video
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()