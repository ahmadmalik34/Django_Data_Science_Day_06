import numpy as np
from datetime import datetime

def load_stock_data(filepath):
    data=np.genfromtxt(filepath,delimeter=',',skip_header=1)
    dates=data[:,0]
    open=data[:,1]
    highs=data[:,2]
    lows=data[:,3]
    closes=data[:,4]
    volumes=data[:,5]
    return{
        'dates':dates,
        'open':open,
        'highs':highs,
        'lows':lows,
        'closes':closes,
        'volumes':volumes
    }
def calculate_statistics(stock_data):
    pass

def find_best_worst_days(stock_data):
    pass

def generate_signals(stock_data):
    pass
def generate_report(stock_data, stats, best_day, worst_day, ma, signals):
    pass
def main():
     print("🚀 Starting Stock Market Analysis with NumPy...\n")
    
    print("📁 Loading stock data...")
    stock_data = load_stock_data('data/stock_data.csv')
    print(f"✅ Loaded {len(stock_data['dates'])} days of data\n")

       print("📁 Loading stock data...")
    stock_data = load_stock_data('data/stock_data.csv')
    print(f"✅ Loaded {len(stock_data['dates'])} days of data\n")
    
    # Calculate statistics
    print("📊 Calculating statistics...")
    stats = calculate_statistics(stock_data)
    
    # Find best/worst days
    print("🔍 Analyzing best and worst trading days...")
    best_day, worst_day = find_best_worst_days(stock_data)
    
    # Generate signals
    print("💡 Generating trading signals...")
    ma, signals = generate_signals(stock_data)
    
    # Generate and print report
    report = generate_report(stock_data, stats, best_day, worst_day, ma, signals)
    print(report)
    
    # Save report to file
    with open('stock_analysis_report.txt', 'w') as f:
        f.write(report)
    print("✅ Report saved to 'stock_analysis_report.txt'")

if __name__ == '__main__':
    main()