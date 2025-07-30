# QR Code Generator

**Two main functions:**
1. Generate QR codes from CSV data (PNG files)
2. Convert PNG to ZPL format for Zebra printer printing

## Quick Start

1. **Setup**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare CSV file** (`urls.csv`)
   ```csv
   id,url,SerialNumber
   1,https://example.com/item1,ABC123
   2,https://example.com/item2,XYZ789
   ```

3. **Generate QR codes**
   ```bash
   python generate_qrs.py
   ```

   Output: PNG files saved in `qr_codes/` folder

## Features

- 🏷️ QR codes with custom labels
- 📁 Batch processing from CSV
- 🖨️ Zebra printer support
- 🧹 Auto-cleanup of old files

## Zebra Printer Setup

To test printing to your Zebra printer:

1. Update the file path and IP address in `zebra_print_example.py`
2. Run: `python zebra_print_example.py`

## Files

- `generate_qrs.py` - **Main QR generator** (CSV → PNG)
- `zebra_image_print.py` - **PNG to ZPL converter** for Zebra printers
- `zebra_print_example.py` - Test Zebra printer setup
- `urls.csv` - Input data (id, url, SerialNumber)
- `qr_codes/` - Generated PNG output 