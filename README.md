# Stock Market Pattern Recognition

## Research Projects: Stock Chart and Wyckoff Pattern Recognition Using Artificial Intelligence (AI/Deep Learning) 

This set of projects aims to revolutionize technical analysis in the stock market by leveraging **Machine Learning (ML)** and **Deep Learning** to transform subjective chart interpretation into a fast, unbiased, quantitative analysis system.

---

## Phase 1: General Information & Objectives

### 1.1 Project Details

| Project | Topic |
| :--- | :--- |
| **Project 1** | Stock Market recognition Wyckoff using Machine Learning |
| **Project 2** | Stock market chart pattern recognition using deep learning |


### 1.3 Objectives

* **Wyckoff Project:**
    * To develop an automated system that can accurately detect and flag key Wyckoff events (e.g., Selling Climax, Automatic Rally, Spring, and Upthrust After Distribution) in stock price data.
    * To create a prototype platform for traders to use automated Wyckoff analysis tools.
* **Chart Pattern Project:**
    * To develop an Automated Trading System (ATS) using Machine Learning that can learn from historical data.
    * To adapt to market situations in real time.

---

## Phase 2: Science Technology and Innovation

### 2.1 Innovation Highlights

The main innovation is the use of **AI in FinTech** to automate financial analysis.

| List | Currently available [cite: 75, 240] | New technology use  |
| :--- | :--- | :--- |
| **Pattern Recognition** | Manual analysis by traders | Automated AI-driven detection [cite: 75, 240] |
| **Accuracy** | Subject to human error  | High precision with deep learning  |
| **Adaptability** | Static rule-based approach  | Dynamic learning from market trends  |

### 2.2 Core Technology Used (Related Work & Tools)

| Technology | Project | Description/Tool |
| :--- | :--- | :--- |
| **Deep Learning Models** | Chart Pattern | **CNNs** for OHLC-recognition and **LSTMs** for time-series analysis. |
| **Algorithmic Detection** | Wyckoff | Develops a set of rules and algorithms to identify Wyckoff Key Events (SC, AR, Spring, UTAD). |
| **Forecasting Model** | Both | Uses **LSTM** (Long Short-Term Memory) to predict price movement direction. |
| **Data Source** | Both | **SETTREAD API** – Provides historical stock prices, OHLC data, and technical indicators. |
| **Frameworks** | Both | **Python** as the language; **TensorFlow / PyTorch** for Deep Learning; **Pandas & NumPy** for data processing. |
| **Deployment** | Both | **Google Cloud / AWS** for model hosting; **Flask/FastAPI** for API-based services. |

---

## Phase 3: Methodology (CRISP-DM)

Both projects utilize the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology.

### 3.1 Conceptual Framework

`Data Collection → Data Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment` 

### 3.2 CRISP-DM Phases

| Phase | Key Activities  |
| :--- | :--- |
| **1. Business Understanding** | Develop a Deep Learning model to classify price chart patterns and reduce errors in predicting market trends. |
| **2. Data Understanding** | Data comes from a database, which may be stock or crypto data. Includes Personalized Data (user investment behavior). |
| **3. Data Preparation** | **Exploratory Data Analysis (EDA)**[cite: 109, 275]; **Data Manipulation** (cleaning data); **Feature Engineering** (creating new features like RSI, MACD)[cite: 113, 279]; **Normalization** (scaling data to an appropriate range)[cite: 116, 282]. |
| **4. Modeling** | Use a Machine Learning or Deep Learning model (CNN, LSTM or Transformer) to classify chart types. |
| **5. Evaluation** | Use **MAPE (Mean Absolute Percentage Error)** to measure the model's error. Decide whether to improve the model. |
| **6. Deployment** | Show the model's results using a chart (Chart Patterns Visualization). Examples include the "Head and Shoulders" pattern. |

---

## Phase 4: Business Information (Business Model Canvas)

The business strategy is based on the Business Model Canvas.

| Component | Shared Strategy  |
| :--- | :--- |
| **Value Propositions** | Automated Pattern Detection, Backtesting for Strategies. |
| **Customer Segments** | Retail Traders, Professional Traders. |
| **Channels** | APIs for Brokers, Social Media & Ads, Web & Mobile Apps[cite: 153, 319]. |
| **Revenue Streams** | Subscription Plans. |
| **Key Partners** | Settrade Api, Regulatory Bodies, Brokerage Firms[cite: 141, 307]. |
| **Key Resources** | Financial Data, Technical Team, AI models. |
| **Key Activities** | Model Development, Platform Development, Data Integration. |
| **Cost Structure** | Technology Development, Data Acquisition Costs, Cloud Infrastructure. |

---

## Phase 5: Proposal Schedule and Indicators

### 5.1 Gantt Chart (12-Month Plan)

| Detail | Month 1-3 | Month 4-6 | Month 7-9 | Month 10-12 |
| :--- | :--- | :--- | :--- | :--- |
| **Planning & Research** | Phase 1: General Information & Planning, Phase 2: Technology Research & Model Selection  | | | |
| **Data & Modeling** | Phase 3: Data Collection & Preprocessing  | Phase 3: Model Development & Training  | Phase 3: Model Testing & Evaluation  | |
| **Business & Deployment** | Phase 4: Business Model & Strategy Planning  | | | Phase 3 & 4: Deployment & Implementation  |
| **Completion** | | | | Final Proposal Completion & Presentation  |

### 5.2 Key Performance Indicators (KPIs)

| Key Result | KPI (Metric for Measurement) | Target | Timeline |
| :--- | :--- | :--- | :--- |
| **Data Collection & Preprocessing** | Percentage of required stock market data collected and cleaned | 100% complete |Month 3  |
| **Model Training & Initial Evaluation** | Model accuracy on training data | ≥ 70% accuracy | Month 6  |
| **Model Optimization & Improvement** | Model accuracy on test data | ≥ 85% accuracy | Month 8  |
| **Prototype Deployment & Testing** | Functional AI model deployed for stock pattern recognition | Deployed & functional | Month 10  |
| **System Efficiency** | Model inference time per prediction | < 1 second per prediction | Month 11  |

---

## Project Visualization (Result Examples)

### Wyckoff Zones Prediction

*Example of Wyckoff zone detection (Accumulation/Distribution) and key events (SC, AR, Spring) in PTT and BTC:*




### Chart Pattern Recognition

*Example of Head and Shoulders (IH&S) pattern detection in BTC:*