import cv2
import os

# Ruta del video
video_path = "video_prueba.mp4" 
output_folder = "frames_extraidos"

os.makedirs(output_folder, exist_ok=True)
cap = cv2.VideoCapture(video_path)

count = 0
fps = int(cap.get(cv2.CAP_PROP_FPS)) # Cuántos cuadros por segundo tiene el video

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Guardar un fotograma cada medio segundo
    if count % (fps // 2) == 0: 
        frame_name = os.path.join(output_folder, f"frame_{count}.jpg")
        cv2.imwrite(frame_name, frame)
    
    count += 1

cap.release()
print("Los fotogramas se han guardado en la carpeta:", output_folder)