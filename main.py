import requests
import re
import json
from langchain.schema import Document
from fpdf import FPDF

def scrape_columbia_spectator_article(url: str) -> Document:
    response = requests.get(url)
    html = response.text

    # Step 1: Extract the Fusion.globalContent JavaScript block
    match = re.search(r'Fusion\.globalContent\s*=\s*({.*?})\s*;', html, re.DOTALL)
    if not match:
        raise ValueError("Could not find globalContent in the page.")

    # Step 2: Parse the JSON
    json_text = match.group(1)
    data = json.loads(json_text)

    # Step 3: Pull out article text
    content_elements = data.get("content_elements", [])
    paragraphs = [item["content"] for item in content_elements if item.get("type") == "text"]
    text = "\n\n".join(paragraphs)

    return Document(page_content=text, metadata={"source": url})

import unicodedata

def clean_text(text: str) -> str:
    # Replace common smart punctuation
    replacements = {
        "’": "'", "‘": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "…": "...",
        "•": "*", "©": "(c)", "®": "(R)"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)

    # Remove any remaining non-latin-1 characters (like \u200b)
    return ''.join(c for c in text if ord(c) < 256)



def save_to_pdf(document: Document, output_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", 'B', 14)
    pdf.multi_cell(0, 10, clean_text(f"Source: {document.metadata['source']}"))
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for paragraph in document.page_content.split("\n\n"):
        pdf.multi_cell(0, 10, clean_text(paragraph))
        pdf.ln()

    pdf.output(output_path)

# Example usage:
url = "https://www.columbiaspectator.com/news/2025/06/16/khalils-first-direct-statement-to-the-court-released/"
doc = scrape_columbia_spectator_article(url)
save_to_pdf(doc, "khalil_article.pdf")



