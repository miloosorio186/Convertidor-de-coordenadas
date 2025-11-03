# Convertidor-de-coordenadas
Convierte coordenadas Geodesicas a Rectangulares y muestra el punto en google maps

Este programa permite:
✅ Convertir coordenadas geodésicas (Latitud φ, Longitud λ, Altura h) a coordenadas cartesinas ECEF (X, Y, Z).
✅ Generar automáticamente un enlace a Google Maps con un marcador (pin) en la ubicación ingresada.
✅ Mostrar las coordenadas convertidas en pantalla.

📁 1. Requisitos del sistema

✔ Python 3 instalado (3.8 o superior recomendado).
✔ Sistema operativo: Linux / Windows / MacOS.
✔ No requiere instalación de librerías adicionales.

⚙️ 2. Cómo ejecutar el programa

Guarda el archivo con el nombre geo.py.

Abre una terminal o consola en la carpeta donde está el archivo.

Ejecuta con:

python3 geo.py

⌨️ 3. ¿Qué datos debes ingresar?

El programa solicita las coordenadas geodésicas en formato grados, minutos, segundos (DMS):

Latitud (φ) → Norte (+) / Sur (−)

Longitud (λ) → Este (+) / Oeste (−)

Altura (h) → En metros sobre el elipsoide (no sobre el nivel del mar)

Ejemplo:

Grados latitud (φ): 4
Minutos latitud: 56
Segundos latitud: 33
Grados longitud (λ): 75
Minutos longitud: 34
Segundos longitud: 23
Altura sobre el elipsoide (m): 3450

🧠 4. ¿Qué hace el programa internamente?

Convierte coordenadas de ° ' " (grados, minutos, segundos) a grados decimales.

Usa el modelo WGS84, estándar global de GPS.

Calcula las coordenadas ECEF (Earth-Centered, Earth-Fixed):

𝑋
=
(
𝑁
+
ℎ
)
cos
⁡
(
𝜑
)
cos
⁡
(
𝜆
)
X=(N+h)cos(φ)cos(λ)

𝑌
=
(
𝑁
+
ℎ
)
cos
⁡
(
𝜑
)
sin
⁡
(
𝜆
)
Y=(N+h)cos(φ)sin(λ)

𝑍
=
(
𝑁
(
1
−
𝑒
2
)
+
ℎ
)
sin
⁡
(
𝜑
)
Z=(N(1−e
2
)+h)sin(φ)

Genera un enlace de Google Maps con marcador exacto (lat, lon).

Intenta abrir automáticamente el navegador web.

🗺️ 5. Visualización en Google Maps

✔ El enlace se genera con formato:

https://www.google.com/maps?q=LATITUD,LONGITUD


Este formato asegura que aparezca un PIN (marcador rojo) en la ubicación.

📍 6. Datos que muestra el programa
📌 Coordenadas ECEF (rectangulares):
X = 1584070.14 m
Y = -6157522.97 m
Z = 546146.61 m

📍 Enlace con punto en Google Maps:
https://www.google.com/maps?q=4.9425,-75.573055
✅ Abriendo navegador con el punto exacto...

📂 7. Estructura del archivo
📁 Proyecto/
 ├── geo.py        # Código principal
 └── README.md     # Documentación (este archivo)

✅ 8. Estado actual del proyecto

✔ Funciona correctamente con:

Conversión de Geodésicas → Cartesianas (ECEF)

Generación y apertura de enlace Google Maps con marcador

Entrada manual de datos por consola

❌ (Opcionales futuros que se pueden agregar más adelante):

Gráfico 3D del elipsoide de la Tierra

Exportar a archivo .txt o .csv

Soporte para coordenadas con N/S/E/O automáticas

Menú interactivo para múltiples conversiones