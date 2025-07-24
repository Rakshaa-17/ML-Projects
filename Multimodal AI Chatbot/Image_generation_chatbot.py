import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import requests

# Initialize the GenAI client
client = genai.Client(api_key="")  # Replace with your actual API key or environment variable

# Streamlit app configuration
st.set_page_config(page_title="GenAI Chatbot", layout="centered")
st.title("GenAI Image Chatbot")
st.markdown("Generate images, edit images, or ask questions about uploaded images.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image" in message:
            st.image(message["image"], width=300)

# User input form
with st.form(key="user_input_form"):
    user_input = st.text_input("Enter a prompt to generate/edit an image or ask about an uploaded image:")
    uploaded_file = st.file_uploader("Upload an image (optional, for editing or understanding):", type=["jpg", "jpeg", "png"])
    mode = st.radio("Select mode:", ["Generate Image", "Edit Image", "Understand Image"])
    submit_button = st.form_submit_button(label="Submit")

# Process user input
if submit_button and (user_input or uploaded_file):
    if mode == "Understand Image" and uploaded_file:
        # Image understanding mode
        with st.chat_message("user"):
            st.markdown(user_input)
            st.image(uploaded_file, width=300, caption="Uploaded Image")
        
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "image": uploaded_file
        })

        # Process uploaded image for understanding
        try:
            image_bytes = uploaded_file.read()
            image = types.Part.from_bytes(
                data=image_bytes, mime_type="image/jpeg"
            )
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[user_input, image],
            )
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            # Add assistant response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.text
            })
        
        except Exception as e:
            with st.chat_message("assistant"):
                st.error(f"Error processing image: {str(e)}")
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Error: {str(e)}"
            })

    elif mode == "Edit Image" and uploaded_file and user_input:
        # Image editing mode
        with st.chat_message("user"):
            st.markdown(user_input)
            st.image(uploaded_file, width=300, caption="Original Image")
        
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "image": uploaded_file
        })

        # Process uploaded image for editing
        try:
            image_bytes = uploaded_file.read()
            image = Image.open(BytesIO(image_bytes))
            image.verify()  # Verify it's a valid image
            image = Image.open(BytesIO(image_bytes))  # Reopen after verify
            
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=[user_input, image],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
            
            # Process response
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    with st.chat_message("assistant"):
                        st.markdown(part.text)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": part.text
                    })
                elif part.inline_data is not None:
                    try:
                        # Check if data is base64-encoded
                        data = part.inline_data.data
                        try:
                            data = base64.b64decode(data)
                        except base64.binascii.Error:
                            pass
                        
                        # Validate and process image
                        edited_image = Image.open(BytesIO(data))
                        edited_image.verify()  # Verify it's a valid image
                        edited_image = Image.open(BytesIO(data))  # Reopen after verify
                        
                        # Save and display edited image
                        edited_image.save('edited_image.png')
                        with st.chat_message("assistant"):
                            st.image('edited_image.png', width=300, caption="Edited Image")
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": "Edited image",
                            "image": 'edited_image.png'
                        })
                    except Exception as img_error:
                        with st.chat_message("assistant"):
                            st.error(f"Failed to process edited image: {str(img_error)}")
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": f"Error: Failed to process edited image: {str(img_error)}"
                        })
        
        except Exception as e:
            with st.chat_message("assistant"):
                st.error(f"Error editing image: {str(e)}")
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Error: {str(e)}"
            })

    elif mode == "Generate Image" and user_input:
        # Image generation mode
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Generate image based on text prompt
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=user_input,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
            
            # Process response
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    with st.chat_message("assistant"):
                        st.markdown(part.text)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": part.text
                    })
                elif part.inline_data is not None:
                    try:
                        # Check if data is base64-encoded
                        data = part.inline_data.data
                        try:
                            data = base64.b64decode(data)
                        except base64.binascii.Error:
                            pass
                        
                        # Validate and process image
                        image = Image.open(BytesIO(data))
                        image.verify()  # Verify it's a valid image
                        image = Image.open(BytesIO(data))  # Reopen after verify
                        
                        # Save and display image
                        image.save('temp_image.png')
                        with st.chat_message("assistant"):
                            st.image('temp_image.png', width=300, caption="Generated Image")
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": "Generated image",
                            "image": 'temp_image.png'
                        })
                    except Exception as img_error:
                        with st.chat_message("assistant"):
                            st.error(f"Failed to process generated image: {str(img_error)}")
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": f"Error: Failed to process generated image: {str(img_error)}"
                        })
        
        except Exception as e:
            with st.chat_message("assistant"):
                st.error(f"Error generating image: {str(e)}")
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Error: {str(e)}"
            })

# Instructions for users
st.markdown("""
### How to Use:
1. **Generate an Image**: Select 'Generate Image', enter a descriptive prompt (e.g., "A dragon flying over a futuristic city"), and click Submit.
2. **Edit an Image**: Select 'Edit Image', upload an image, enter an edit prompt (e.g., "Add a llama next to me"), and click Submit.
3. **Understand an Image**: Select 'Understand Image', upload an image, enter a question (e.g., "What is in this image?"), and click Submit.
""")
