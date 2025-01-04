import streamlit as st
import os
import openai
from preprocessor import extract_frames, get_frame_embeddings
from scene_generator import generate_summary_and_dialogue

# Load API key from environment variables or .env file
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("Movie Scene Summarizer and Dialogue Generator")

if openai.api_key is None:
    st.error("OpenAI API key is missing. Set it in a .env file or as an environment variable.")
else:
    # Video upload
    uploaded_video = st.file_uploader("Upload a Movie Video", type=["mp4", "avi", "mov"])

    if uploaded_video is not None:
        # Save the uploaded video in a temporary folder
        temp_dir = "temp_video"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        video_path = os.path.join(temp_dir, uploaded_video.name)
        with open(video_path, "wb") as f:
            f.write(uploaded_video.read())

        # Display the uploaded video
        st.video(video_path)

        # Process video to extract frames
        st.write("Extracting frames from the video...")
        frames = extract_frames(video_path, num_frames=5)
        st.write(f"Extracted {len(frames)} frames.")

        # Generate frame embeddings
        st.write("Generating embeddings for the frames...")
        frame_embeddings = get_frame_embeddings(frames)
        st.write("Generated embeddings:", frame_embeddings)

        # Generate summary and dialogues for the video
        scene_description = st.text_area(
            "Enter a scene description or context:",
            "A tense conversation between two characters, one trying to persuade the other."
        )
        if st.button("Generate Summary and Dialogues"):
            st.write("Generating scene summary and dialogues...")
            result = generate_summary_and_dialogue(scene_description)
            st.write("### Scene Summary and Dialogue Options")
            st.text(result)
