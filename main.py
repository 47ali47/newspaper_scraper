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

    print("CMDDDD", cmd)

    try:
        result = subprocess.run(
            cmd, 
            check=True, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError:
        print("Failed to generate PDF")
    

if __name__ == "__main__":
    # important to have .pdf in the name of the otput
    urlToPDF(url="https://www.columbiaspectator.com/opinion/2024/05/16/the-palestine-exception/", output="article_1.pdf")

    # PDF of newspaper is converted into a string with its text
    # extracted_text = extract_text("palestine_exception_article.pdf")
    # the text is analyzed by LLM acting as researcher
    # print(text_analyzer(extracted_text))

    



