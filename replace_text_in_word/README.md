# PDF Date Replacer

This Python script replaces a specific date string inside a PDF file, preserving its layout, structure, and font alignment (supports Hebrew right-to-left). The modified PDF is saved to a new file.

---

## ✅ Features

- Replaces only the **first** occurrence of a target date string in the document.
- Paints over the original text and inserts the new one at the same location.
- Supports **Hebrew / RTL text**, including font embedding via `.ttf` fonts.
- Automatically reduces font size if text doesn't fit.

---

## 🛠 Requirements

Only one Python package is required:

```bash
pip install PyMuPDF
```

All other packages that may have been used during testing (like `pdf2docx`, `PySimpleGUI`, etc.) are not needed for this final version.

You can clean up your environment by uninstalling:

```
pip uninstall docx2pdf fire fonttools lxml numpy opencv-python-headless pdf2docx PySimpleGUI python-docx pywin32 termcolor tqdm typing_extensions
```

---

## 🚀 Usage

```python
replace_date_in_pdf(
    pdf_path="path/to/input.pdf",
    output_path="path/to/output.pdf",
    old_date="14.1.2024",
    new_date="14.07.2025",
    font_path="C:/Windows/Fonts/arial.ttf"  # Optional but recommended for Hebrew
)
```

---

## 🔧 Parameters

| Parameter           | Description                                                    |
|---------------------|----------------------------------------------------------------|
| `pdf_path`          | Full path to your input PDF file                               |
| `output_path`       | Path to save the modified PDF                                  |
| `old_date`          | The exact text of the date to search and replace               |
| `new_date`          | The new date string to insert                                  |
| `font_path`         | Optional: TTF font file path (e.g. Arial)                      |
| `starting_font_size`| Starting size (defaults to 12), will decrease down to size 8   |

---

## 📌 Notes

- Only replaces the **first matching instance**.
- Will skip replacement if the font doesn't fit.
- Paints over the original with white before inserting new text.

---

## 📄 License

MIT License