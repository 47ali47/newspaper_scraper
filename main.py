# Chrome Shell Code
# alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# chrome --headless --disable-gpu --print-to-pdf https://www.columbiaspectator.com/news/2025/06/16/khalils-first-direct-statement-to-the-court-released/

# Imports to convert shell code into python code
import subprocess
import argparse

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

def save_text_to_pdf(text: str, filename: str):
    html = f"<pre>{text}</pre>"
    HTML(string=html.write_pdf(filename))


if __name__ == "__main__":
    # important to have .pdf in the name of the otput
    urlToPDF(url="https://www.columbiaspectator.com/opinion/2024/05/16/the-palestine-exception/", output="article_1.pdf")
    extracted_text = extract_text("article_1.pdf")
    analyzed_text = text_analyzer(extracted_text)
    print(analyzed_text)
    save_text_to_pdf(analyzed_text, "article_1_cleaned.pdf")




    



