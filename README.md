# 📈 AI-Driven Stock Market Pattern Recognition

## 🌟 โครงการวิจัย: การจดจำรูปแบบแผนภูมิและ Wyckoff ในตลาดหุ้นด้วยปัญญาประดิษฐ์ (AI/Deep Learning)

ชุดโครงการนี้มุ่งเน้นการปฏิวัติการวิเคราะห์ทางเทคนิคในตลาดหุ้น โดยการใช้ประโยชน์จาก Machine Learning (ML) และ Deep Learning เพื่อแปลงการตีความแผนภูมิแบบอัตนัย (Subjective) ให้เป็นระบบวิเคราะห์เชิงปริมาณ (Quantitative Analysis) ที่รวดเร็ว แม่นยำ และเป็นกลาง

---

## 🎯 Phase 1: General Information & Objectives

### 1.1 ข้อมูลโครงการหลัก

| โครงการ | ชื่อภาษาไทย | ชื่อภาษาอังกฤษ |
| :--- | :--- | :--- |
| **โครงการที่ 1** | [cite_start]การตรวจจับเหตุการณ์ Wyckoff และแนวโน้มตลาดหุ้นด้วยแมชชีนเลิร์นนิง [cite: 36] | [cite_start]Stock Market recognition Wyckoff using Machine Learning [cite: 35] |
| **โครงการที่ 2** | [cite_start]การจดจำรูปแบบแผนภูมิตลาดหุ้นโดยใช้การเรียนรู้เชิงลึก [cite: 202] | [cite_start]Stock market chart pattern recognition using deep learning [cite: 201] |

### 1.2 ผู้จัดทำและที่ปรึกษา

| บทบาท | ชื่อ-สกุล | สังกัด |
| :--- | :--- | :--- |
| **ผู้ตรวจสอบ** | [cite_start]Hilman Yusoh [cite: 60, 227] | [cite_start]Student ID: 651437006 [cite: 60, 227] |
| **ที่ปรึกษา** | [cite_start]Kholed Langsari [cite: 62, 229] | [cite_start]Email: langsari@ftu.ac.th [cite: 62, 229] |

### 1.3 วัตถุประสงค์ (Objectives)

* [cite_start]**Wyckoff Project:** พัฒนาระบบอัตโนมัติที่สามารถตรวจจับเหตุการณ์ Wyckoff หลัก (เช่น Selling Climax, Spring, Upthrust After Distribution) ในข้อมูลราคาหุ้นได้อย่างแม่นยำ [cite: 64] [cite_start]และสร้างแพลตฟอร์มต้นแบบสำหรับใช้เครื่องมือวิเคราะห์ Wyckoff อัตโนมัติ [cite: 65]
* [cite_start]**Chart Pattern Project:** พัฒนาระบบ ATS โดยใช้ Machine Learning ที่สามารถเรียนรู้จากข้อมูลในอดีต [cite: 220] [cite_start]และปรับให้เข้ากับสถานการณ์ตลาดแบบเรียลไทม์ [cite: 221]

---

## 🔬 Phase 2: Science Technology and Innovation

### 2.1 สารัตถะนวัตกรรม

[cite_start]นวัตกรรมหลักคือการใช้ **Machine Learning/Deep Learning** ใน **FinTech** เพื่อเปลี่ยนการตีความแผนภูมิที่เป็นอัตนัย ให้กลายเป็นระบบวิเคราะห์เชิงปริมาณที่รวดเร็วและไม่มีอคติ [cite: 57, 69, 224]

| รายการ | สิ่งที่มีอยู่ในปัจจุบัน (Currently available) | สิ่งที่ใช้ใหม่ในโครงการ (New technology use) |
| :--- | :--- | :--- |
| **การจดจำรูปแบบ** | [cite_start]การวิเคราะห์ด้วยมือโดยเทรดเดอร์ [cite: 73, 241] | [cite_start]การตรวจจับอัตโนมัติด้วย AI [cite: 73, 241] |
| **ความแม่นยำ** | [cite_start]ขึ้นอยู่กับความผิดพลาดของมนุษย์ [cite: 73, 241] | [cite_start]ความแม่นยำสูงด้วย Deep Learning [cite: 73, 241] |
| **การปรับตัว** | [cite_start]วิธีการแบบคงที่ (Static rule-based approach) [cite: 73, 241] | [cite_start]การเรียนรู้แบบไดนามิกจากแนวโน้มตลาด (Dynamic learning from market trends) [cite: 73, 241] |

### 2.2 เทคโนโลยีหลักที่ใช้ (New Ideas or Technology)

| เทคโนโลยี | โครงการที่ใช้ | รายละเอียด |
| :--- | :--- | :--- |
| **Algorithmic Detection** | Wyckoff | [cite_start]พัฒนาชุดกฎและอัลกอริทึมเพื่อระบุเหตุการณ์ Wyckoff Key Events (SC, AR, Spring) โดยวิเคราะห์ **Structure-Volume-Price** [cite: 70, 77] |
| **Deep Learning (LSTM)** | [cite_start]ทั้งสองโครงการ [cite: 71, 78, 237, 244] | [cite_start]ใช้ Long Short-Term Memory (LSTM) ซึ่งเป็นโครงข่ายประสาทเทียมสำหรับประมวลผลข้อมูลอนุกรมเวลา (Time Series Data) เพื่อคาดการณ์ทิศทางราคาในอนาคต [cite: 71, 78] |
| **Deep Learning (CNN)** | [cite_start]Chart Pattern [cite: 237, 244] | [cite_start]ใช้ Convolutional Neural Networks (CNNs) ในการวิเคราะห์ภาพแผนภูมิ (OHLC-recognition) [cite: 237, 244] |
| **Database** | Wyckoff | [cite_start]ใช้ **Apache Cassandra** ซึ่งเป็น NoSQL database แบบกระจายสำหรับจัดเก็บข้อมูลแท่งเทียน (candlestick data) ที่มีปริมาณมาก [cite: 76] |

---

## 📝 Phase 3: Methodology (CRISP-DM)

โครงการใช้ระเบียบวิธี **CRISP-DM (Cross-Industry Standard Process for Data Mining)** ซึ่งมี 6 ขั้นตอนหลัก:

### 3.1 Conceptual Framework

[cite_start]`Data Collection → Data Preprocessing → Feature Engineering → Model Training → Evaluation → Deployment` [cite: 93, 260]

### 3.2 CRISP-DM Phases

| Phase | กิจกรรมหลัก |
| :--- | :--- |
| **1. Business Understanding** | [cite_start]พัฒนา Deep Learning Model เพื่อจำแนกประเภทรูปแบบแผนภูมิและลดข้อผิดพลาดในการคาดการณ์แนวโน้มตลาด [cite: 99, 100, 101, 267, 268] |
| **2. Data Understanding** | [cite_start]รวบรวมข้อมูลราคาหุ้น/คริปโต และข้อมูลส่วนบุคคล (พฤติกรรมการลงทุนของผู้ใช้) [cite: 104, 105, 106, 271, 272, 273] |
| **3. Data Preparation** | [cite_start]**Feature Engineering:** สร้างคุณลักษณะใหม่ เช่น RSI, MACD, Moving Average [cite: 112, 113, 279, 280] [cite_start]**Normalization:** ปรับมาตราส่วนข้อมูลให้อยู่ในช่วงที่เหมาะสม (0-1 หรือ -1 ถึง 1) [cite: 115, 116, 282, 283] |
| **4. Modeling** | [cite_start]ใช้โมเดล Deep Learning (CNN, LSTM, Transformer) เพื่อจำแนกรูปแบบแผนภูมิ (Chart Pattern Classification) [cite: 119, 120, 121, 286, 287, 288] |
| **5. Evaluation** | [cite_start]ใช้ **MAPE (Mean Absolute Percentage Error)** ในการวัดข้อผิดพลาดของโมเดล [cite: 123, 124, 290, 291] [cite_start]และตัดสินใจปรับปรุงโมเดลหากข้อผิดพลาดสูง [cite: 125, 126, 292, 293] |
| **6. Deployment** | [cite_start]แสดงผลลัพธ์ของโมเดลผ่านการแสดงผลรูปแบบแผนภูมิ (Chart Patterns Visualization) และจุดกลับตัวของแนวโน้ม [cite: 129, 133, 296, 300] |

---

## 💼 Phase 4: Business Information (Business Model Canvas)

| องค์ประกอบ | [cite_start]Wyckoff Project [cite: 137-158] | [cite_start]Chart Pattern Project [cite: 304-325] |
| :--- | :--- | :--- |
| **1) Value Propositions** | [cite_start]Automated Pattern Detection, Backtesting for Strategies [cite: 137, 304] | [cite_start]Automated Pattern Detection, Backtesting for Strategies [cite: 137, 304] |
| **3) Key Partners** | [cite_start]Settrade Api, Regulatory Bodies, Brokerage Firms [cite: 140, 307] | [cite_start]Settrade Api, Regulatory Bodies, Brokerage Firms [cite: 140, 307] |
| **4) Key Resources** | [cite_start]Financial Data, Technical Team, Ai models [cite: 143, 310] | [cite_start]Financial Data, Technical Team, Ai models [cite: 143, 310] |
| **5) Customer Segments** | [cite_start]Retail Traders, Professional Traders [cite: 144, 311] | [cite_start]Retail Traders, Professional Traders [cite: 144, 311] |
| **9) Revenue Streams** | [cite_start]Subscription Plans [cite: 158, 325] | [cite_start]Subscription Plans [cite: 158, 325] |

---

## 📅 Phase 5: Proposal Schedule and Indicators

### 5.1 Gantt Chart (แผน 12 เดือน)

| Detail | Month 1-3 | Month 4-6 | Month 7-9 | Month 10-12 |
| :--- | :--- | :--- | :--- | :--- |
| **Planning & Research** | [cite_start]Phase 1 & 2 [cite: 163, 330] | | | |
| **Data & Modeling** | [cite_start]Data Collection & Preprocessing [cite: 163, 330] | [cite_start]Model Development & Training [cite: 163, 330] | [cite_start]Model Testing & Evaluation [cite: 163, 330] | |
| **Business & Deployment** | [cite_start]Business Model & Strategy Planning [cite: 163, 330] | | | [cite_start]Deployment & Implementation [cite: 163, 330] |
| **Completion** | | | | [cite_start]Final Proposal Completion & Presentation [cite: 163, 330] |

### 5.2 Key Performance Indicators (KPIs)

| Key Result | KPI (Metric for Measurement) | Target | Timeline |
| :--- | :--- | :--- | :--- |
| **Model Training & Initial Evaluation** | [cite_start]Model accuracy on training data [cite: 165, 332] | [cite_start]≥ 70% accuracy [cite: 165, 332] | [cite_start]Month 6 [cite: 165, 332] |
| **Model Optimization & Improvement** | [cite_start]Model accuracy on test data [cite: 165, 332] | [cite_start]≥ 85% accuracy [cite: 165, 332] | [cite_start]Month 8 [cite: 165, 332] |
| **Prototype Deployment & Testing** | [cite_start]Functional AI model deployed for stock pattern recognition [cite: 165, 332] | [cite_start]Deployed & functional [cite: 165, 332] | [cite_start]Month 10 [cite: 165, 332] |
| **System Efficiency** | [cite_start]Model inference time per prediction [cite: 165, 332] | [cite_start]< 1 second per prediction [cite: 165, 332] | [cite_start]Month 11 [cite: 165, 332] |

---

## 🖼️ Project Visualization (ตัวอย่างผลลัพธ์)

### Wyckoff Zones Prediction

*ตัวอย่างการตรวจจับโซน Wyckoff (Accumulation/Distribution) และเหตุการณ์หลัก (SC, AR, Spring) ในหุ้น PTT และ BTC:*




### Chart Pattern Recognition

*ตัวอย่างการตรวจจับรูปแบบแผนภูมิ Head and Shoulders (IH&S) ใน BTC:*