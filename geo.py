import math
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo  # Para abrir HTML con el gráfico

# === Conversión de Coordenadas Geodésicas a Cartesianas (ECEF) ===
def dms_a_decimal(grados, minutos, segundos):
    return grados + minutos / 60 + segundos / 3600

def geodesicas_a_ecef(phi, lam, h):
    a = 6378137.0            # Semieje mayor (WGS84)
    e2 = 0.00669437999014    # Excentricidad²

    phi = math.radians(phi)
    lam = math.radians(lam)

    N = a / math.sqrt(1 - e2 * math.sin(phi)**2)

    X = (N + h) * math.cos(phi) * math.cos(lam)
    Y = (N + h) * math.cos(phi) * math.sin(lam)
    Z = (N * (1 - e2) + h) * math.sin(phi)
    
    return X, Y, Z

# === Solo genera el link de Google Maps, NO abre navegador ===
def generar_link_google_maps(lat, lon):
    return f"https://www.google.com/maps?q={lat},{lon}"

# === Gráfico 3D del elipsoide WGS84 y el punto ===
def graficar_elipsoide_y_punto(Xp, Yp, Zp):
    a = 6378137.0       # Semieje mayor
    b = 6356752.3142    # Semieje menor

    # Malla del elipsoide
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = a * np.outer(np.cos(u), np.sin(v))
    y = a * np.outer(np.sin(u), np.sin(v))
    z = b * np.outer(np.ones_like(u), np.cos(v))

    fig = go.Figure()

    fig.add_trace(go.Surface(
        x=x, y=y, z=z,
        opacity=0.7,
        colorscale="Earth",
        showscale=False
    ))

    fig.add_trace(go.Scatter3d(
        x=[Xp], y=[Yp], z=[Zp],
        mode='markers',
        marker=dict(size=6, color='red'),
        name='Punto'
    ))

    fig.update_layout(
        title="🌍 Elipsoide WGS84 con punto geográfico",
        scene=dict(aspectmode='data'),
        margin=dict(l=0, r=0, t=40, b=0)
    )

    # Abre el gráfico en el navegador como HTML
    pyo.plot(fig, filename='elipsoide.html', auto_open=True)

# === Programa Principal ===
if __name__ == "__main__":
    print("=== Conversión de Coordenadas + Gráfico 3D ===")

    phi_g = float(input("Grados latitud (φ): "))
    phi_m = float(input("Minutos latitud: "))
    phi_s = float(input("Segundos latitud: "))

    lam_g = float(input("Grados longitud (λ): "))
    lam_m = float(input("Minutos longitud: "))
    lam_s = float(input("Segundos longitud: "))

    h = float(input("Altura sobre el elipsoide (m): "))

    # Conversión
    lat_decimal = dms_a_decimal(phi_g, phi_m, phi_s)
    lon_decimal = -dms_a_decimal(lam_g, lam_m, lam_s)  # Longitud Oeste = negativa

    X, Y, Z = geodesicas_a_ecef(lat_decimal, lon_decimal, h)

    print("\n📌 Coordenadas ECEF (X, Y, Z) en metros:")
    print(f"X = {X}")
    print(f"Y = {Y}")
    print(f"Z = {Z}")

    # 1️⃣ Primero grafica
    graficar_elipsoide_y_punto(X, Y, Z)

    # 2️⃣ Luego muestra el link (sin abrir navegador)
    link = generar_link_google_maps(lat_decimal, lon_decimal)
    print("\n🔗 Enlace para ver en Google Maps:")
    print(link)
