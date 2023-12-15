import streamlit as st

st.set_page_config(page_title="Streamlit App", page_icon=":smiley:")
st.title("Image White Balancing")

uploaded_file = st.file_uploader(
    label="Upload an image file to white balance", type=["png", "jpg"]
)

if uploaded_file is not None:
    data = {
        "Name": uploaded_file.name,
        "Size": str(round((uploaded_file.size / 1024**2), 2)) + " MB",
        "Rype": uploaded_file.type,
    }
    # To read file as bytes:
    st.write(data)
    st.image(uploaded_file)
