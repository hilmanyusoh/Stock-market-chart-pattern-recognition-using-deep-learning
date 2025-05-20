# 📈 Stock Market Chart Pattern Recognition using Deep Learning

This project aims to detect classical stock chart patterns — specifically the **Head and Shoulders** pattern — using **Deep Learning (CNN)** on candlestick chart data.

By leveraging Convolutional Neural Networks, the model can learn visual features from candlestick patterns and automatically highlight potential reversal zones on stock charts. This can help traders and investors make more informed decisions.

---

## 🚀 Project Objectives

- Automatically recognize **Head and Shoulders** patterns from historical candlestick data
- Build a pipeline using Deep Learning (CNN) for time-series pattern classification
- Store and retrieve financial data using Cassandra
- Display results with candlestick visualizations and pattern markers

---

## 🧠 Technologies Used

- Python 3
- TensorFlow / Keras
- Cassandra (NoSQL Database)
- Docker & Docker Compose
- Pandas, Numpy, Plotly, Matplotlib
- Jupyter Notebooks

---

## 🗂️ Project Structure

| File/Folder                  | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| `fetch_candlestick_data.ipynb` | Retrieves stock data in candlestick format                |
| `connect_cassandra.ipynb`      | Stores and queries data from Cassandra database           |
| `sample_data.ipynb`            | Example data for testing the pattern detection algorithm  |
| `chartpattern/`                | Core logic and CNN model code                             |
| `docker-compose.yml`          | Environment setup using Docker                            |

---

## 📊 Sample Output

The model will highlight chart pattern points as:

- 🟡 **Left Shoulder**
- 🔴 **Head**
- 🟢 **Right Shoulder**

Candlestick plots will display detected patterns over time.

---

