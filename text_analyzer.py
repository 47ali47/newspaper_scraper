import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


# Google Gemini LLM acts a researcher looking for evidence of chilling effect in the newspaper text

def text_analyzer(text_input):

    # load environment variables from .env file (requires `python-dotenv`)
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

    # Chat with the Model, setting up LLM as a researcher (SystemMessage)
    # The newspaper text is inputted into the model (HumanMessage)
    messages = [
        SystemMessage("You are a researcher looking for evidence, if it exists, of chilling effects and suppresion of pro-Palestine protests. Return in bullet points exact quotations of supporting evidence. Also return a brief summary of the text."),
        HumanMessage(text_input),
    ]
    # Save the response from LLM and print out content
    response = model.invoke(messages)
    print(response.content)