# Detección y Conteo de Cajas de Cartón con YOLOv8 y Streamlit

> Sistema inteligente de Computer Vision basado en fine-tuning de **YOLOv8m** para la detección y conteo en tiempo real de cajas de cartón, integrado con una interfaz web interactiva.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8m-Ultralytics-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## Descripción General
Este proyecto automatiza la inspección logística mediante visión artificial. Permite entrenar un modelo personalizado para reconocer cajas de cartón, probarlo mediante scripts de consola con contadores en tiempo real, y desplegar una aplicación web interactiva para facilitar su uso.

---

## Arquitectura y Descripción de Scripts

El proyecto se compone de los siguientes módulos principales:

### 1. `train.py` (Entrenamiento)
* **¿Qué hace?:** Realiza el *fine-tuning* del modelo base `yolov8m.pt` adaptándolo específicamente para reconocer y etiquetar cajas de cartón a partir de un dataset personalizado.
* **Librerías:** `ultralytics` (YOLO), `os`.
* **Ejecución:** Carga el modelo, el archivo de configuración del dataset (`data.yaml`) y ejecuta el entrenamiento mediante el método `.train()`.

### 2. `test_detector.py` (Pruebas de Detección)
* **¿Qué hace?:** Pone a prueba el modelo entrenado con videos de prueba o la cámara en tiempo real (`0`), filtrando detecciones con un umbral de confianza mínimo.
* **Librerías:** `ultralytics`, `OpenCV (cv2)`, `os`.
* **Ejecución:** 
  - Carga los pesos del modelo (`YOLO()`).
  - Abre la fuente de video (`cv2.VideoCapture()`).
  - Analiza cada fotograma con un umbral de confianza y dibuja las cajas detectadas (`results[0].plot()`).
  - Muestra el resultado en una ventana interactiva (`cv2.imshow()`).

### 3. `test_contador.py` (Contador en Tiempo Real)
* **¿Qué hace?:** Extiende el script anterior añadiendo un contador dinámico que calcula la cantidad exacta de cajas presentes en cada fotograma del video.
* **Librerías:** `ultralytics`, `OpenCV (cv2)`, `os`.
* **Ejecución:**
  - Obtiene los FPS originales del video para una reproducción fluida (`cv2.CAP_PROP_FPS`).
  - Cuenta las cajas detectadas en el frame (`len(results[0].boxes)`).
  - Dibuja el texto del contador en tiempo real (`cv2.putText()`) y permite pausar o salir con la tecla `"q"`.

### 4. `app.py` (Interfaz Web en Streamlit)
* **¿Qué hace?:** Eleva el proyecto a una aplicación web interactiva donde se puede subir un video, ajustar el umbral de confianza, controlar la velocidad de reproducción y visualizar el análisis de forma cómoda en el navegador.
* **Librerías:** `ultralytics`, `OpenCV`, `tempfile`, `time`, `PIL`, `streamlit`, `os`.
* **Ejecución:**
  - Configura la página web y su barra lateral de controles.
  - Carga el modelo con caché de recursos de Streamlit.
  - Almacena temporalmente el video subido para procesarlo fotograma a fotograma y renderizarlo en tiempo real en la interfaz gráfica.
 
  - <img width="1893" height="945" alt="Captura de pantalla 2026-10-27 183324" src="https://github.com/user-attachments/assets/62caab44-bc47-4951-b6bb-ec3bdd85eac5" />

  # YOLOv8 Box Detector
Fine-tuning de YOLOv8m para detección y conteo en tiempo real de cajas de cartón con interfaz en Streamlit.

[![Streamlit App](https://yolov8-box-detector-2ugtyfyqqq2zumdm2aechc.streamlit.app/)

