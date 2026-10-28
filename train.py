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
        data=os.path.join(BASE_DIR, "boxes.v1i.yolov8", "data.yaml"),  # Ubicación del dataset (Se cambió a uno mas grande)
        epochs=25,                         # Número de épocas de entrenamiento
        imgsz=640,                         # Tamaño de la imagen
        batch=16,                          # Tamaño del lote
        device=0,                          # Para forzar el uso de la GPU (índice 0:)
        project=os.path.join(BASE_DIR, "mis_resultados"),  # Ruta donde se guardá el entrenamiento
        name="pallet_boxes_exp"            # Subcarpeta donde se guardan los resultados
    )

    print("El entrenamiento ha finalizado")

if __name__ == '__main__':
    main()