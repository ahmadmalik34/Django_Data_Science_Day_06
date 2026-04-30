# Day 6: Stock Analysis with NumPy

This project demonstrates how to use the NumPy library in Python to perform a basic analysis of stock data. The analysis includes calculating the average closing price, the highest and lowest prices, and the daily returns.

## Features

-   **Data Loading**: Loads stock data from a CSV file using NumPy.
-   **Data Analysis**:
    -   Calculates the average closing price of the stock.
    -   Finds the highest and lowest stock prices in the dataset.
    -   Computes the daily returns to measure volatility.
-   **Reporting**: Saves the analysis results to a text file.

## How to Run

1.  **Clone the repository.**
2.  **Navigate to the `Day_06_NumPy_Stock_Analysis` directory.**
3.  **Install dependencies:**
    ```bash
    pip install numpy
    ```
4.  **Run the analysis script:**
    ```bash
    python analysis.py
    ```
5.  The results of the analysis will be saved in `stock_analysis_report.txt`.

## Data

The `data/stock_data.csv` file contains sample stock data with the following columns: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`.
