# 🛍️ Best Seller Predictor

A machine learning project that predicts the probability of a product being a best seller based on:

- Product Price
- Shipping Cost
- Marketing Rating
- Material Quality

The project uses **Logistic Regression implemented from scratch using NumPy** and provides a simple **Streamlit web interface** for making predictions.

## 🚀 Features

- Logistic Regression implemented from scratch
- Gradient Descent optimization
- Feature scaling
- Numerical stability handling
- Interactive Streamlit interface
- Probability-based prediction

## 🧠 How It Works

The model takes four input features:

| Feature | Description |
|---|---|
| Product Price | Price of the product |
| Shipping Cost | Shipping cost |
| Marketing Rating | Marketing effectiveness rating (1–10) |
| Material Quality | Material quality rating (1–10) |

The features are scaled using the mean and standard deviation calculated during training.

The trained weights are then used to calculate the probability using the sigmoid function.

## 🛠️ Technologies Used

- Python
- NumPy
- Streamlit
- Git & GitHub

## 📂 Project Structure

```text
best_seller_predictor/
│
├── app.py
├── model.py
├── train.py
├── .gitignore
└── README.md