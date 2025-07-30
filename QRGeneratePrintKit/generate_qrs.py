import qrcode
import pandas as pd
import os
import glob
from PIL import Image, ImageDraw, ImageFont
from zebra_image_print import print_png_to_zebra  # אם שמרת את המודול כקובץ נפרד


    
# 📂 Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "qr_codes")
os.makedirs(output_dir, exist_ok=True)

# 🧹 Clear old files
old_files = glob.glob(os.path.join(output_dir, "*.png"))
for f in old_files:
    os.remove(f)
print(f"🧹 Cleared {len(old_files)} old QR files from '{output_dir}'")

# 📄 Load CSV
csv_path = os.path.join(script_dir, "urls.csv")
try:
    df = pd.read_csv(csv_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(csv_path, encoding="cp1255")

print("📄 Loaded CSV preview:")
print(df.to_string(index=False))

# 🅰 Load font
try:
    font = ImageFont.truetype("arial.ttf", size=20)
except:
    font = ImageFont.load_default()

# 🔁 Generate QR per row
for _, row in df.iterrows():
    device_id = str(row['id'])
    url = str(row['url'])
    SerialNumber = str(row['SerialNumber'])

    print(f"\n📌 Generating QR for device: {device_id}")
    print("🔗 URL:", url)
    print("🔖 Serial Number:", SerialNumber)

    # Create QR
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4
    )
    qr.clear()
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Measure text widths
    serial_text = SerialNumber
    url_text = url

    draw_dummy = ImageDraw.Draw(qr_img)
    serial_bbox = draw_dummy.textbbox((0, 0), serial_text, font=font)
    url_bbox = draw_dummy.textbbox((0, 0), url_text, font=font)

    serial_width = serial_bbox[2] - serial_bbox[0]
    url_width = url_bbox[2] - url_bbox[0]
    max_text_width = max(serial_width, url_width)

    qr_width, qr_height = qr_img.size
    padding = 40  # Extra margin

    # New image width = max between QR and text width + padding
    final_width = max(qr_width, max_text_width + padding)
    text_height = 80  # Enough for both lines

    total_height = qr_height + text_height
    final_img = Image.new("RGB", (final_width, total_height), "white")

    # Center QR horizontally in new image
    qr_x = (final_width - qr_width) // 2
    final_img.paste(qr_img, (qr_x, 0))

    # Draw text centered
    draw = ImageDraw.Draw(final_img)

    # Serial
    serial_x = (final_width - serial_width) // 2
    draw.text((serial_x, qr_height + 10), serial_text, fill="black", font=font)

    # URL
    url_x = (final_width - url_width) // 2
    draw.text((url_x, qr_height + 35), url_text, fill="black", font=font)

    # Save
    safe_serial = "".join(c for c in SerialNumber if c.isalnum() or c in ('_', '-'))
    filename = os.path.join(output_dir, f"{safe_serial}.png")
    final_img.save(filename)
    print(f"✅ Saved: {filename}")
