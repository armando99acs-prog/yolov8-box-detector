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

# Se obtienen los fps del video original
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) if fps > 0 else 30

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Fin del video o no se pudo acceder a la fuente.")
        break

    # Se analiza el video cada frame
    results = model(frame, conf=0.8)

    # Se obtiene el numero de cajas en el frame actual
    boxes = results[0].boxes
    cantidad_cajas = len(boxes)

    # Señala cada caja dentro de un cuadro
    annotated_frame = results[0].plot()

    # Se dibuja un texto con el contador
    texto_contador = f"Cajas detectadas en cuadro: {cantidad_cajas}"
    cv2.putText(
        annotated_frame, 
        texto_contador, 
        (15, 25),                      # Coordenada (X, Y)
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.60,                          # Escala de la letra
        (0, 255, 0),                   # Color Verde 
        2,                             # Grosor de la línea
        cv2.LINE_AA
    )

    # Muestra el video analizado en tiempo real
    cv2.imshow("Sistema de Inspeccion Logistica - IA", annotated_frame)

    # Controla la velocidad de reproducción del video. Tambien lo aborta con la tecla "q"
    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()