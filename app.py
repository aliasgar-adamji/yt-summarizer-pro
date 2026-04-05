import streamlit as st
import processor
import zipfile
import io

st.set_page_config(page_title="YT Summarizer Pro", layout="wide")

st.title("📺 YouTube Link Summarizer")
st.caption("Generate professional articles and downloadable websites from videos.")

url = st.text_input("Paste YouTube URL here:")

if st.button("Generate Content") and url:
    with st.spinner("Processing video... This may take a minute for long videos."):
        raw_output = processor.process_youtube_content(url)
        
        try:
            # Parsing the output from Gemini
            article = raw_output.split("---MARKDOWN---")[1].split("---HTML---")[0].strip()
            html_code = raw_output.split("---HTML---")[1].split("---CSS---")[0].strip()
            css_code = raw_output.split("---CSS---")[1].split("---JS---")[0].strip()
            js_code = raw_output.split("---JS---")[1].strip()

            # Display Article
            st.divider()
            st.markdown(article)

            # Create Zip in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                zip_file.writestr("index.html", html_code)
                zip_file.writestr("style.css", css_code)
                zip_file.writestr("script.js", js_code)
            
            st.sidebar.success("Generation Complete!")
            st.sidebar.download_button(
                label="📁 Download Webpage Zip",
                data=zip_buffer.getvalue(),
                file_name="summarized_article.zip",
                mime="application/zip"
            )
        except Exception as e:
            st.error(f"Error parsing output: {e}")
            st.write("Full raw output for debugging:", raw_output)