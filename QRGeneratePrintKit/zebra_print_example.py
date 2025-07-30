import os
from zebra_image_print import print_png_to_zebra  # make sure this module is in your project

# Get the base directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the folder containing the QR images
qr_folder = os.path.join(script_dir, "qr_codes")


# IP of the Zebra printer
zebra_ip = "10.0.21.178"

# Loop through all .png files in the folder
for filename in os.listdir(qr_folder):
    if filename.lower().endswith(".png"):
        image_path = os.path.join(qr_folder, filename)
        print(f"🖨️ Sending '{filename}' to Zebra printer...")

        try:
            print_png_to_zebra(image_path, zebra_ip=zebra_ip)
            print("✅ Printed successfully!\n")
        except Exception as e:
            print(f"❌ Failed to print '{filename}': {e}\n")
