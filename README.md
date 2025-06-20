# newspaper_scraper
Scrape college newspapers articles 

Main.py: extracts text from a URL link, and calls text_analyzer.py

text_analyzer.py: uses LangChain to input extracted text into Gemini model acting as a researcher looking for evidence of chilling effect. Returns summary and key evidence in quotations
