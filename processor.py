import os
from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def process_youtube_content(url):
    # 1. Fetch Transcript
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
    docs = loader.load()
    if not docs:
        return "No transcript found."
    
    full_text = docs[0].page_content

    # 2. Chunking (For long videos)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    chunks = text_splitter.split_text(full_text)

    # 3. Summarize Chunks with Groq (Speed)
    groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
    chunk_summaries = []
    
    summary_prompt = ChatPromptTemplate.from_template(
        "Summarize the following technical transcript segment concisely: {text}"
    )
    summary_chain = summary_prompt | groq_llm | StrOutputParser()

    for chunk in chunks:
        summary_chunk = summary_chain.invoke({"text": chunk})
        chunk_summaries.append(summary_chunk)
    
    combined_context = "\n\n".join(chunk_summaries)

    # 4. Generate Final Article & Web-code with Gemini (Creativity)
    gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    
    final_prompt = ChatPromptTemplate.from_template("""
    You are a Senior Technical Writer. Using the context below, perform two tasks:
    1. Write a professional, engaging Medium-style article in Markdown.
    2. Create a production-ready HTML/CSS/JS single-page website to display this article with professional level of beautification.

    Context: {context}

    OUTPUT FORMAT (MUST FOLLOW EXACTLY):
    ---MARKDOWN---
    [Your article here]
    ---HTML---
    [HTML code]
    ---CSS---
    [CSS code]
    ---JS---
    [JS code]
    """)

    final_chain = final_prompt | gemini_llm | StrOutputParser()
    return final_chain.invoke({"context": combined_context})