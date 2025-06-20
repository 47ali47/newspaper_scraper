# Chrome Shell Code
# alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# chrome --headless --disable-gpu --print-to-pdf https://www.chromestatus.com/

from pypdf import PdfReader
from fpdf import FPDF

# Extracts text from the export PDF from the internet
def extract_text(pdf):
    reader = PdfReader(pdf)
    texts = (page.extract_text() for page in reader.pages)
    output = "\n".join(texts)
    return output

# Returns a pdf of the cleaned text
# note, had to download DejaVuSans unicode text from online
def text_to_pdf(text_input: str, output_name: str):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font('DejaVuSans', '', "fonts/DejaVuSans.ttf")
    pdf.set_font('DejaVuSans', '', 12) # Example font settings
    # split on newlines and wrap long lines automatically
    for line in text_input.splitlines():
        pdf.multi_cell(0, 8, line)
    
    pdf.output(output_name)

def extraction_process(pdf, cleaned_pdf):
    text_to_pdf(extract_text(pdf), cleaned_pdf)

if __name__ == "__main__":
    # article = extract_text("output.pdf")
    # print(article)
    extraction_process("output.pdf", "cbia.pdf")


