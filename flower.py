import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def draw_flower(rgb_color):
    # Create a blank white canvas
    canvas = np.ones((400, 400, 3), dtype=np.uint8) * 255

    # Draw flower with RGB color
    petal_color = tuple(map(int, rgb_color))
    cv2.circle(canvas, (200, 200), 50, petal_color, -1)
    cv2.circle(canvas, (200, 150), 50, petal_color, -1)
    cv2.circle(canvas, (150, 200), 50, petal_color, -1)
    cv2.circle(canvas, (250, 200), 50, petal_color, -1)
    cv2.circle(canvas, (200, 250), 50, petal_color, -1)

    # Convert to PIL Image for display in Streamlit
    pil_image = Image.fromarray(canvas)

    return pil_image

def main():
    st.title("RGB Flower Drawer")

    # Sliders for RGB values
    r = st.slider("Red", 0, 255, 128, step=1)
    g = st.slider("Green", 0, 255, 128, step=1)
    b = st.slider("Blue", 0, 255, 128, step=1)

    # Draw flower and display in Streamlit
    rgb_color = (r, g, b)
    flower_image = draw_flower(rgb_color)

    st.image(flower_image, caption="Drawn Flower", use_column_width=True)

if __name__ == "__main__":
    main()
