import math
import webbrowser

# === Conversión de Coordenadas Geodésicas a Cartesianas (ECEF) ===
def dms_a_decimal(grados, minutos, segundos):
    return grados + minutos / 60 + segundos / 3600

def geodesicas_a_ecef(phi, lam, h):
    # WGS84
    a = 6378137.0            # Semieje mayor
    e2 = 0.00669437999014    # Excentricidad al cuadrado

    phi = math.radians(phi)
    lam = math.radians(lam)

    N = a / math.sqrt(1 - e2 * math.sin(phi)**2)

    X = (N + h) * math.cos(phi) * math.cos(lam)
    Y = (N + h) * math.cos(phi) * math.sin(lam)
    Z = (N * (1 - e2) + h) * math.sin(phi)
    
    return X, Y, Z

# === Abrir Google Maps MOSTRANDO UN PUNTO (PIN) ===
def abrir_google_maps_con_pin(lat, lon):
    url = f"https://www.google.com/maps?q={lat},{lon}"
    print(f"\n📍 Enlace con punto en Google Maps:")
    print(url)

    try:
        webbrowser.open(url)  # Abre el navegador
        print("✅ Abriendo navegador con el punto exacto...")
    except:
        print("⚠ No se pudo abrir automáticamente. Copia y pega el enlace en tu navegador.")

# === 3. Programa Principal ===
if __name__ == "__main__":
    print("=== Conversión de Coordenadas Geodésicas a Cartesianas + Google Maps ===")

    # Entrada de coordenadas
    phi_g = float(input("Grados latitud (φ): "))
    phi_m = float(input("Minutos latitud: "))
    phi_s = float(input("Segundos latitud: "))

    lam_g = float(input("Grados longitud (λ): "))
    lam_m = float(input("Minutos longitud: "))
    lam_s = float(input("Segundos longitud: "))

    h = float(input("Altura sobre el elipsoide (m): "))

    # Conversión a decimales
    lat_decimal = dms_a_decimal(phi_g, phi_m, phi_s)
    lon_decimal = -dms_a_decimal(lam_g, lam_m, lam_s)  # Longitud Oeste = negativa

   
    X, Y, Z = geodesicas_a_ecef(lat_decimal, lon_decimal, h)

    print("\n Coordenadas ECEF (rectangulares):")
    print(f"X = {X} m")
    print(f"Y = {Y} m")
    print(f"Z = {Z} m")

   
    abrir_google_maps_con_pin(lat_decimal, lon_decimal)
