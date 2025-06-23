# Chrome Shell Code
# alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# chrome --headless --disable-gpu --print-to-pdf https://www.columbiaspectator.com/news/2025/06/16/khalils-first-direct-statement-to-the-court-released/

# Imports to convert shell code into python code
import subprocess
import argparse
from fpdf import FPDF
from pypdf import PdfReader
from text_analyzer import text_analyzer

# Extracts text from the export PDF from the internet
def extract_text(pdf):
    reader = PdfReader(pdf)
    texts = (page.extract_text() for page in reader.pages)
    output = "\n".join(texts)
    return output

# Convert a URL into a PDF 
def urlToPDF(
        url: str,
        output: str,
        chrome_path: str = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
    parser = argparse.ArgumentParser(
    )

    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output}",
        url
    ]

    try:
        result = subprocess.run(
            cmd, 
            check=True, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError:
        print("Failed to generate PDF")

# text to pdf
def text_to_pdf(text, output):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", "/Users/anboli/Downloads/dejavu-fonts-ttf-2.37/ttf/DejaVuSansCondensed.ttf")
    pdf.set_font("DejaVu", size=10)

    # Add the string content to the PDF
    pdf.multi_cell(0, 10, txt=text) # 0 for width means full page width, 10 for line height
    # Save the PDF
    pdf.output(output)
    print("PDF created successfully with the string content.")

# important to have .pdf in the name of the otput
def run_extraction(url, output):
    urlToPDF(url, output)
    extracted_text = extract_text(output)
    # add the URL into the final PDF output for cross-checking
    extracted_text += url
    # run LLM analysis on text
    analyzed_text = text_analyzer(extracted_text)
    # print(analyzed_text)
    text_to_pdf(analyzed_text, output)

if __name__ == "__main__":
    run_extraction("https://www.columbiaspectator.com/opinion/2024/05/16/the-palestine-exception/", "article_1.pdf")




    



