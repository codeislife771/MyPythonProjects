from PIL import Image
import socket
import os
import textwrap

def image_to_grf(image_path, grf_name="MYIMG.GRF"):
    img = Image.open(image_path).convert("L").point(lambda x: 0 if x < 128 else 255, mode='1')
    width, height = img.size

    # Width in bytes (1 byte = 8 pixels)
    width_bytes = (width + 7) // 8

    # Raw binary data
    data = bytearray()
    for y in range(height):
        byte = 0
        bits = 0
        for x in range(width):
            pixel = img.getpixel((x, y))
            bit = 0 if pixel else 1  # 0 = white, 1 = black
            byte = (byte << 1) | bit
            bits += 1
            if bits == 8:
                data.append(byte)
                byte = 0
                bits = 0
        if bits > 0:
            byte <<= (8 - bits)
            data.append(byte)

    # Convert binary to hex
    hex_data = ''.join(f"{byte:02X}" for byte in data)
    wrapped = '\n'.join(textwrap.wrap(hex_data, 64))  # ZPL prefers line-wrapping

    total_bytes = len(data)
    bytes_per_row = width_bytes

    # Build the ~DG and ^XG ZPL command
    zpl = f"""~DG{grf_name},{total_bytes},{bytes_per_row},{wrapped}
^XA
^FO50,50^XG{grf_name},2,2^FS
^XZ
"""
    return zpl

def send_zpl_to_zebra(zebra_ip, zpl_code, port=9100):
    with socket.socket() as s:
        s.connect((zebra_ip, port))
        s.sendall(zpl_code.encode('utf-8'))
    print("📤 ZPL sent to printer at", zebra_ip)

def print_png_to_zebra(png_path, zebra_ip="192.168.1.100", grf_name="MYIMG.GRF"):
    zpl = image_to_grf(png_path, grf_name=grf_name)
    send_zpl_to_zebra(zebra_ip, zpl)
