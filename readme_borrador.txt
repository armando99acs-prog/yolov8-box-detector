---------train.py----------
¿Qué hace?
Hace un finetunig del modelo Yolov8m.pt para reconocer cajas de cartón

¿Qué librerías usa?
ultralytics. Es donde se encuentran los modelos YOLO

¿Cómo se ejecuta?
Se carga el modelo, el dataset y la ubicación para guardar los resultados
y se entrena con .train

--------test_detector.py---------
¿Qué hace?
Pone a prueba el modelo previamente entrenado

¿Qué librerías usa?
ultralytics. La librería de YOLO para análisis de video
OpenCV (cv2). Librería para la visión artificial y el procesamiento de imágenes

¿Cómo se ejecuta?
model = YOLO() se carga el modelo
cv2.VideoCpature() abre un video previamente grabado. 0 para usar camara
results = model(frame, conf=0.5) Analiza cada frame del video y solo señala
las cajas cuya confianza sea mayor o igual a 50
annotated_frame = results[0].plot() Dibuja los cuadros donde señala las cajas
cv2.imshow Muestra el video en pantalla ya analizado
cv2.waitKey Permite abortar el video


---------test_contador-----------
¿Qué hace?
Añade un contador de cajas cada frame del video

¿Qué librerías usa?
las mismas de Ultralyticts y OpenCV

¿Cómo se ejecuta?
fps = cap.get(cv2.CAP_PROP_FPS) se obtienen los fps del video original
boxes = results[0].boxes Obtiene el numero de cajas en cada frame
cv2.putText() Se dibuja el contador en video en tiempo real
if cv2.waitKey(delay) & 0xFF == ord("q"): delay controla los FPS del video final
pero sigue controlando abortar el analisis con la tecla "q"

------------app.py------------
¿Qué hace?
Se pasa de ejecutar el modelo en Python a una pagina web donde se puede controlar
la velocidad del video y es mas cómodo de visualizar

¿Qué librerías usa?
ultralytics y OpenCV
tempfile. Para guardar archivos temporales
time. Para controlar la velocidad de reproducción del video
PIL. Manejo y procesamiento de imágenes
streamlit. Permite crear paginas web usando únicamente Python

¿Cómo se ejecuta?
Se configura la pagina y se escribe el titulo, el tipo de layout y la barra
lateral
Se carga el modelo y el video y se guarda en archivos temporales para
su análisis 
En una ventana superior se puede visualizar el video original
Con un botón se abre otra ventana abajo donde se visualiza el video analizado
donde se puede observar los recuadros que encapsulan a las cajas