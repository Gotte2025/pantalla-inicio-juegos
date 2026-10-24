import sys
from pathlib import Path
import qrcode

if len(sys.argv) != 2:
    print('Uso: python generar_qr.py "https://tu-usuario.github.io/pantalla-inicio-juegos/"')
    raise SystemExit(2)

url = sys.argv[1].strip()
if not url.startswith("https://"):
    print("Aviso: para instalar como PWA, usá una dirección HTTPS pública.")
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=4)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
out = Path("QR_PantallaInicio_Juegos.png")
img.save(out)
print(f"QR guardado en: {out.resolve()}")
print(f"Destino: {url}")
