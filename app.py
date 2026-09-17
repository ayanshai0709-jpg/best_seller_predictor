import streamlit as st
import numpy as np

from model import train_model, predict


st.title("🛍️ Best Seller Predictor")

st.write("Enter the details of your product below.")


price = st.number_input(
    "Product Price (₹)",
    min_value=0.0
)

shipping = st.number_input(
    "Shipping Cost (₹)",
    min_value=0.0
)

marketing = st.slider(
    "Marketing Rating",
    1,
    10,
    5
)

material = st.slider(
    "Material Quality",
    1,
    10,
    5
)


if st.button("Predict"):

    w, b, mu, sigma = train_model()

    product = np.array([
        [price, shipping, marketing, material]
    ])

    product_scaled = (product - mu) / sigma

    probability = predict(
        product_scaled,
        w,
        b
    )

    percentage = probability[0] * 100

    st.success(
        f"Best Seller Probability: {percentage:.4f}%"
    )
