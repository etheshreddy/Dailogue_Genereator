# import openai

# def generate_summary_and_dialogue(scene_description):
#     try:
#         # Refined prompt for better outputs
#         prompt = (
#             f"Scene Description: {scene_description}\n"
#             f"Task: Summarize this scene in 2-3 sentences and create three distinct dialogues between the characters based on the scene's tone and context."
#         )

#         # OpenAI GPT-3.5 Turbo API call
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # Updated to a supported model
#             messages=[
#                 {"role": "system", "content": "You are an expert movie scriptwriter."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=500,  # Control output length
#             temperature=0.7  # Control creativity
#         )

#         # Extract generated text
#         generated_text = response['choices'][0]['message']['content'].strip()
#         return generated_text
#     except Exception as e:
#         return f"Error generating summary and dialogues: {str(e)}
# 
import os
import google.generativeai as genai

API_KEY = "AIzaSyCdIuGl0ZqbSNF15lA_U6ScJn8j8snjbkc"
MODEL = "models/gemini-pro"

def generate_custom_text(prompt, temperature=0.7, max_output_tokens=256, top_p=None, top_k=None):
    if not API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable must be set.")

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None

def generate_summary_and_dialogue(scene_description):
    try:
        prompt = (
            f"Scene Description: {scene_description}\n"
            f"Task: Summarize this scene in 2-3 sentences and create three distinct dialogues between the characters based on the scene's tone and context."
        )
        print(prompt)
        generated_text = generate_custom_text(prompt=prompt) # Corrected line
        return generated_text # Corrected line
    except Exception as e:
        return f"Error generating summary and dialogues: {str(e)}"

if __name__ == "__main__":
    scene = "A tense standoff in a dusty saloon. Two cowboys face each other, hands hovering over their holsters. The clock strikes noon."
    result = generate_summary_and_dialogue(scene)
    if result:
        print(result)
    else:
        print("Failed to generate summary and dialogue.")   