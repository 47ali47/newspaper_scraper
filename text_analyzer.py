import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


# Google Gemini LLM acts as a researcher looking for evidence of chilling effect in the newspaper text

def text_analyzer(text_input):
    
    # load the LLM model
    model = intialize_model()
   
    # Chat with the Model, setting up LLM as a researcher (SystemMessage)
    # The newspaper text is inputted into the model (HumanMessage)
    messages = [
        SystemMessage("""
You are a meticulous researcher. Your task is to find and present evidence, if it exists, of chilling effects and suppression of pro-Palestine protests.

Structure your response clearly for easy programmatic PDF export. Use the following format:

### Summary
[A concise, brief summary of the overall findings, without exceeding 150 words. Ensure this summary is a single, continuous paragraph.]

### Supporting Evidence (Exact Quotations)
* "[Exact quotation of supporting evidence.]" 
* "[Exact quotation of supporting evidence. If a quotation is very long (over 150 characters), please aim to break it at a natural pause or punctation and insert ' \\n' (backslash, n) to suggest a line break for readability within a cell. Avoid breaking words. Example: 'This is a very long sentence \\n that needs to be broken for PDF readability.']" 
* [Continue with bullet points for each piece of evidence.]

### Print out the URL at the bottom of the page
**Important Formatting Guidelines for Your Output:**
* **Use markdown headings:** `###` for main sections.
* **Use markdown bullet points:** `*` for evidence quotations.
* **For long quotations:** Strategically insert ` \n` (space, backslash, n) to suggest soft line breaks for PDF tools. This prevents single, unbroken long lines from causing "character too big" errors, especially for URLs or extremely long sentences. Only use this *within* a quotation if it significantly exceeds typical line length (e.g., >150-200 characters) and a natural break point exists. Avoid breaking words mid-word.
* **Maintain clear source attribution** for each quotation.
* **Ensure consistent capitalization and punctuation** as you are providing exact quotations.
* **Do not include any conversational filler** in your response, just the structured output.
                      """),
        HumanMessage(text_input),
    ]
    # Save and return the response from LLM
    response = model.invoke(messages)
    return response.content

# Initialize model once only, returns model 
def intialize_model():
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        key = os.environ.get("GOOGLE_API_KEY")
        
        if not key:
            raise RuntimeError("GOOGLE_API_KEY is not set in the environment.")

        os.environ["GOOGLE_API_KEY"] = os.environ.get("GOOGLE_API_KEY")
    except ImportError:
        print("error")

    # start an AI chat
    model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

    return model
