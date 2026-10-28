import streamlit as st
import cv2
import tempfile
import time  
from ultralytics import YOLO
from PIL import Image
import os  # 1. Importamos la librería os

# Se defina BASE_DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Se configura la página
st.set_page_config(
    page_title="Sistema de Inspección Logística - IA",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("Sistema Inteligente de Conteo Logístico con IA")
st.markdown("### Proyecto de Portafolio - Visión por Computadora y Automatización")
st.write("Sube un video de una banda transportadora o área de almacenamiento para procesar la detección y conteo automático de cajas.")

# Barra lateral para configuraciones
st.sidebar.header("Configuración del Modelo y Reproducción")
conf_threshold = st.sidebar.slider("Umbral de Confianza", 0.1, 1.0, 0.8, 0.05)

# Control de velocidad
speed_factor = st.sidebar.slider("Velocidad de video", 0.5, 2.0, 1.0, 0.5, 
                                 help="Mueve la barra para cambiar la velocidad del video.")

# Abortar video
pause_video = st.sidebar.checkbox("Abortar reproducción")

# Se carga el modelo
@st.cache_resource
def load_model():
    model_path = os.path.join(BASE_DIR, "mis_resultados", "pallet_boxes_exp-4", "weights", "best.pt")
    return YOLO(model_path)

model = load_model()

# Se sube el video
video_file = st.file_uploader("Sube un archivo de video (.mp4)", type=["mp4", "mov", "avi"])

if video_file is not None:
    # Se guarda el video en un arechivo temporal
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    
    # Se muestra el video original
    st.video(video_file)
    
    if st.button("Analizar video con IA"):
        with st.spinner("Procesando fotogramas y calculando métricas..."):
            cap = cv2.VideoCapture(tfile.name)
            
            # Se obtienen los FPS originales del video
            fps = cap.get(cv2.CAP_PROP_FPS)
            if fps == 0 or fps is None:
                fps = 30  
            
            # Se calcula el tiempo de espera por fotograma ajustado por la ralentización
            frame_delay = (1.0 / fps) / speed_factor

            # Contenedor para mostrar el progreso en Streamlit
            st_frame = st.empty()
            
            frame_count = 0
            while cap.isOpened():
                while pause_video:
                    time.sleep(0.1)
                
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Para incrementar el contador de fotogramas
                frame_count += 1
                
                # Salto de fotogramas
                if frame_count % 2 != 0:
                    continue
                
                # Se analiza el fotograma seleccionado
                results = model(frame, conf=conf_threshold)
                annotated_frame = results[0].plot()
                
                # Se convierte el color de BGR (OpenCV) a RGB (Streamlit)
                annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                
                # Se muestra el fotograma procesado en la web
                st_frame.image(annotated_frame, channels="RGB", use_container_width=True)
                
            cap.release()
            st.success("Proceso de inspección completado")
