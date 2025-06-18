#  Imports
import requests # allows access to webpages via HTTP
from bs4 import BeautifulSoup # parses HTML to extract structured data
from langchain.text_splitter import RecursiveCharacterTextSplitter # splits text into chunks for storage
from langchain.schema import Document # stores text and URL