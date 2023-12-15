import streamlit as st

# Setting page configuration, title and icon
st.set_page_config(page_title="Streamlit App", page_icon=":smiley:")
st.title("Image White Balancing")

# Function to upload image
uploaded_file = st.file_uploader(
    label="Upload an image file to white balance", type=["png", "jpg"]
)

# Processes on file after upload
if uploaded_file is not None:
    data = {
        "Name": uploaded_file.name,
        "Size": str(round((uploaded_file.size / 1024**2), 2)) + " MB",
        "Rype": uploaded_file.type,
    }
    # To show file details
    st.write(data)
    st.image(uploaded_file)
