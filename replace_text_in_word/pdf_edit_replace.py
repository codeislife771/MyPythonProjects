import fitz  # PyMuPDF
from pathlib import Path

def replace_date_in_pdf(
    pdf_path,
    output_path,
    old_date,
    new_date,
    font_path="C:/Windows/Fonts/arial.ttf",
    starting_font_size=12
):
    # Ensure input PDF and font file exist
    if not Path(pdf_path).is_file():
        print(f"❌ File not found: {pdf_path}")
        return

    if not Path(font_path).is_file():
        print(f"❌ Font file not found: {font_path}")
        return

    doc = fitz.open(pdf_path)
    replaced = False

    for page in doc:
        words = page.get_text("words")
        for w in words:
            if w[4].strip() == old_date:
                # Define rectangle around the text
                rect = fitz.Rect(w[0], w[1], w[2], w[3])
                # Expand the rectangle slightly to make space
                rect.x0 -= 20
                rect.x1 += 20
                rect.y0 -= 4
                rect.y1 += 4

                # Paint the area white to "erase" old text
                page.draw_rect(rect, fill=(1, 1, 1), color=(1, 1, 1))

                # Try inserting the new date with decreasing font sizes
                for font_size in range(starting_font_size, 7, -1):
                    result = page.insert_textbox(
                        rect,
                        new_date,
                        fontname="CustomFont",
                        fontfile=font_path,
                        fontsize=font_size,
                        color=(0, 0, 0),
                        align=2  # Right-aligned (for RTL)
                    )
                    if result >= 0:
                        print(f"✅ Replaced with: {new_date} (font size {font_size})")
                        replaced = True
                        break
                if not replaced:
                    print("❌ Could not insert the text in the given area.")
                break
        if replaced:
            break

    if replaced:
        doc.save(output_path)
        print(f"📄 Saved updated PDF to: {output_path}")
    else:
        print("⚠️ Target date not found in the document.")


# Example usage
replace_date_in_pdf(
    pdf_path="r.pdf",
    output_path="r_final.pdf",
    old_date="14.1.2024",
    new_date="14.07.2025",
    font_path="C:/Windows/Fonts/arial.ttf"
)
