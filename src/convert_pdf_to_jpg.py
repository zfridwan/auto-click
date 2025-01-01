import fitz  # PyMuPDF
import os

def pdf_to_jpg_with_fitz(pdf_path, output_folder):
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        doc = fitz.open(pdf_path)
        output_files = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            output_file = os.path.join(output_folder, f'page_{page_num + 1}.jpg')
            pix.save(output_file)
            output_files.append(output_file)

        return output_files
    except Exception as e:
        print(f"Kesalahan: {e}")
        raise

# Contoh penggunaan
if __name__ == "__main__":
    input_pdf = r"e:\auto click\src\contoh.pdf"
    output_dir = "output_images"

    try:
        output_files = pdf_to_jpg_with_fitz(input_pdf, output_dir)
        print("Konversi selesai. File JPG disimpan di:")
        for file in output_files:
            print(file)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
