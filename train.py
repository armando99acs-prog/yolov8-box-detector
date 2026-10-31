from ultralytics import YOLO
import os

# Se define BASE_DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    # Se carga el modelo YOLO
    # YOLO descargará los pesos iniciales automáticamente
    model = YOLO("yolov8m.pt")  # yolov8m funcionó mejor que yolov8s

    # Se inicia el entrenamineto
    results = model.train(
        data=os.path.join(BASE_DIR, "dataset", "data.yaml"),  # Ubicación del dataset (Se cambió a uno mas grande)
        epochs=25,                         # Número de épocas de entrenamiento
        #patience=10,                       # Deja de entrenar si en 10 epocas no mejora
        freeze=10,                         # Congela las primeras capas para evitar detectar paredes
        #mosaic=1.0,                        # Mezcla 4 imágenes en 1 para forzar al modelo a ver cajas en contextos caóticos
        #mixup=0.15,                        # Combina imágenes débilmente para difuminar los fondos fijos falsos
        imgsz=640,                         # Tamaño de la imagen
        batch=8,                           # Tamaño del lote
        device=0,                          # Para forzar el uso de la GPU (índice 0:)
        project=os.path.join(BASE_DIR, "mis_resultados"),  # Ruta donde se guardá el entrenamiento
        name="Yolov8m"                     # Subcarpeta donde se guardan los resultados
    )

    print("El entrenamiento ha finalizado")

if __name__ == '__main__':
    main()