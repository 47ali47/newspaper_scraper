# Chrome Shell Code
# alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# chrome --headless --disable-gpu --print-to-pdf https://www.columbiaspectator.com/news/2025/06/16/khalils-first-direct-statement-to-the-court-released/

from pypdf import PdfReader
from fpdf import FPDF

# Extracts text from the export PDF from the internet
def extract_text(pdf):
    reader = PdfReader(pdf)
    texts = (page.extract_text() for page in reader.pages)
    output = "\n".join(texts)
    return output

if __name__ == "__main__":
    # article = extract_text("output.pdf")
    # print(article)
    extract_text("output.pdf")


