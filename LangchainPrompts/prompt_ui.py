from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import streamlit as st
import os
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

import os
os.environ['HF_HOME']="D:/Huggingface_cache"
llm=HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )

)
model=ChatHuggingFace(llm=llm)

# Load environment variables
# load_dotenv()


# token = os.getenv("HF_TOKEN")

# # Hugging Face LLM
# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen3.8-27B",
#     task="text-generation",
#     huggingfacehub_api_token=token,
#     max_new_tokens=512,
#     temperature=0.7
# )

# model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.header("Research Tool")

paper_input = st.selectbox(
    "Select the research paper name",
    [
        "Select..",
        "Attention is All You Need",
        "BERT: Pre-Training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-friendly",
        "Technical",
        "Code-oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# Load prompt
template = load_prompt("template.json")

# Create chain
chain = template | model

# Generate response
# Load prompt
template = load_prompt("template.json")

# Create chain
chain = template | model

if st.button("Summarise"):

    st.write("1. Button clicked")

    if paper_input == "Select..":
        st.warning("Please select a research paper.")

    else:
        st.write("2. Starting chain...")

        with st.spinner("Generating summary..."):

            st.write("3. Calling model...")

            result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            })

            st.write("4. Model returned")

            st.write("Result object:")
            st.write(result)

            st.write("Result content:")
            st.write(result.content)