import streamlit as st
from PIL import Image
from image_shuffler import Shuffler


def shuffle_and_display_image(image_path, matrix_size):
    # Reading the image from local directory to Python environment
    img = Shuffler(image_path)

    # Specifying the matrix to shuffle
    img.shuffle(matrix=matrix_size)

    # Displaying the shuffled image
    st.image(img.show(), caption="Shuffled Image", use_column_width=True)

    # Saving the shuffled image
    img.save()


def main():
    st.title("Image Shuffler App")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Specify the matrix size for shuffling
        matrix_size = (300, 73)

        # Save the uploaded image to a temporary file
        temp_image_path = "temp_image.jpg"
        with open(temp_image_path, "wb") as f:
            f.write(uploaded_file.read())

        # Shuffle and display the image
        shuffle_and_display_image(temp_image_path, matrix_size)


if __name__ == "__main__":
    main()
