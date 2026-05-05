# 📈 Stock Analysis with NumPy

<div align="center">

**Vectorized Numerical Computing for Finance**

[![NumPy](https://img.shields.io/badge/NumPy-2.0%2B-blue?style=flat-square&logo=numpy)](https://numpy.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)

[Features](#-features) • [Installation](#-installation) • [Learn More](#-key-concepts)

</div>

---

## 🎯 Overview

Master NumPy fundamentals by analyzing stock market data. Calculate statistics, detect trends, and generate buy/sell trading signals using vectorized operations.

**See the power of NumPy: 100x faster than Python loops.**

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 📊 **Statistics** | Mean, max, min, std dev, percentiles |
| 📉 **Trend Analysis** | Best/worst trading days |
| 📈 **Moving Averages** | 3-day moving average for trend smoothing |
| 🎯 **Trading Signals** | Buy/sell signals based on moving averages |
| 📝 **Reporting** | Professional ASCII-formatted reports |
| ⚡ **Vectorized Ops** | Pure NumPy — no loops |

---

## 📦 Tech Stack

- **NumPy:** 2.0+
- **Python:** 3.8+
- **Data Format:** CSV

---

## 🚀 Quick Start

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install NumPy
pip install numpy
```

### Run Analysis

```bash
python analysis.py
```

Output file: `stock_analysis_report.txt`

---

## 📊 What It Analyzes

### Price Statistics
```
Mean Price:    $155.42
Max Price:     $160.00
Min Price:     $151.80
Std Dev:       $2.14
```

### Best & Worst Days
```
Best Day:      2024-01-08 (+$2.50)
Worst Day:     2024-01-05 (-$1.80)
```

### Trading Signals
```
3-Day Moving Average detected Buy/Sell signals
Based on price crossovers with the moving average
```

### Volume Analysis
```
Average Volume:  125,400 shares
Total Volume:    1,254,000 shares
```

---

## 🔧 Key NumPy Operations Used

### Array Creation
```python
prices = np.array([155.2, 156.1, 154.8, ...])
```

### Vectorized Statistics
```python
mean_price = np.mean(prices)
max_price = np.max(prices)
std_dev = np.std(prices)
```

### Boolean Indexing
```python
above_avg = prices[prices > np.mean(prices)]
```

### Moving Average (Convolution)
```python
moving_avg = np.convolve(prices, np.ones(3)/3, mode='valid')
```

### Difference Operations
```python
daily_changes = np.diff(prices)
best_day_idx = np.argmax(daily_changes)
```

---

## 📂 Project Structure

```
Day_06_NumPy_Stock_Analysis/
├── analysis.py
├── data/
│   └── stock_data.csv
├── stock_analysis_report.txt
└── README.md
```

---

## 📖 What You'll Learn

✅ NumPy array creation and manipulation  
✅ Broadcasting and vectorized operations  
✅ Statistical functions  
✅ Array indexing and slicing  
✅ Boolean masking  
✅ Aggregation functions  
✅ File I/O with NumPy  
✅ Performance vs Python loops  
✅ Real-world data analysis  

---

## 🧮 NumPy vs Python Loops

### Python Loop (Slow)
```python
total = 0
for price in prices:
    total += price
mean = total / len(prices)
# 1000+ microseconds
```

### NumPy Vectorized (Fast)
```python
mean = np.mean(prices)
# ~10 microseconds
# 100x faster!
```

---

## 💡 Real-World Applications

📈 Finance — Stock analysis, portfolio management  
🏭 Manufacturing — Quality control, defect detection  
🎮 Game Dev — Physics simulations, graphics rendering  
🔬 Science — Signal processing, image analysis  
🏥 Healthcare — Medical imaging, data analysis  

---

## 📚 Data Format

### stock_data.csv
```csv
Date,Open,High,Low,Close,Volume
2024-01-01,155.00,156.50,154.80,155.20,120000
2024-01-02,155.30,157.10,155.00,156.10,125000
```

---

<div align="center">

**Day 6 of 50 — Django × Data Science Challenge**

Mastering NumPy and vectorized computing.

</div>

