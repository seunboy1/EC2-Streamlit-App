import os
import openai
import streamlit as st

openai.api_key= "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"
# os.environ.get('openai_key')

def main():
    st.title("Product Description Generator")
    notes = st.text_area("Enter product information:")
    if st.button("Generate description"):
        with st.spinner("Generating description..."):
            response = openai.completions.create(
              model="text-davinci-003",
              prompt=f"Write a product description based on the below information.\n\n{notes}\n\nDescription:",
              temperature=0.7,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
        description = response.choices[0].text
        st.subheader("Generated description:")
        st.write(description)

if __name__ == "__main__":
    main()