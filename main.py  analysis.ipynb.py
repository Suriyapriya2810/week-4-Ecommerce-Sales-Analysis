import os
import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# 1. LOAD THE DATA
# ==========================================
try:
    df = pd.read_csv("sales_data.csv")
    print("✅ Dataset located successfully!")
except FileNotFoundError:
    print("❌ Error: 'sales_data.csv' not found in this folder.")
    exit()

# ==========================================
# 2. MATCH COLUMNS BY POSITION (Index 0 to 4)
# ==========================================
# Mapping coordinates from your dashboard dataset:
# [0]: Product Name, [1]: Month, [2]: Category, [3]: Total_Sales, [4]: Profit
product_col  = df.columns[0]
month_col    = df.columns[1]
category_col = df.columns[2]
sales_col    = df.columns[3]
profit_col   = df.columns[4]

# ==========================================
# 3. CLEAN DATA & FORCE NUMERIC TYPES 
# ==========================================
# Strips whitespace, removes non-numeric characters, and safely converts to float
df[sales_col] = pd.to_numeric(df[sales_col].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')
df[profit_col] = pd.to_numeric(df[profit_col].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')

# Drop missing rows to keep calculations clean
df = df.dropna(subset=[sales_col, profit_col])

# ==========================================
# 4. CALCULATE MORE METRICS (Advanced Key KPI Indicators)
# ==========================================
total_sales    = df[sales_col].sum()
total_profit   = df[profit_col].sum()
total_orders   = len(df)

# Advanced Metric Calculations
avg_order_value = total_sales / total_orders if total_orders > 0 else 0
profit_margin   = (total_profit / total_sales) * 100 if total_sales > 0 else 0

print("\n=============================================")
print("          📊 E-COMMERCE BUSINESS KPI REPORT     ")
print("=============================================")
print(f"• Total Revenue Generated : ₹ {total_sales:,.2f}")
print(f"• Total Net Profit Earned : ₹ {total_profit:,.2f}")
print(f"• Total Order Volume      : {total_orders} items")
print(f"• Average Order Value(AOV): ₹ {avg_order_value:,.2f}")
print(f"• Net Profit Margin (%)   : {profit_margin:.2f}%")
print("=============================================\n")

# ==========================================
# 5. DATA VISUALIZATION (5 Distinct Charts)
# ==========================================
os.makedirs("visualizations", exist_ok=True)

# Define a larger subplots canvas frame for 5 clean charts (3 rows, 2 columns)
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 18))
axes = axes.flatten() # Flattens the 2D grid into a 1D list to access positions easily (0 to 5)

# --- CHART 1: Bar Chart (Sales by Category) ---
cat_sales = df.groupby(category_col)[sales_col].sum()
cat_sales.plot(kind="bar", color="#1f77b4", edgecolor="black", ax=axes[0])
axes[0].set_title("1. Revenue Contribution by Category", fontsize=12, fontweight="bold")
axes[0].set_ylabel("Sales (₹)")
axes[0].tick_params(axis='x', rotation=30)
axes[0].grid(axis="y", linestyle="--", alpha=0.5)

# --- CHART 2: Line Chart (Sales Volume Trend Over Months) ---
# Ensuring clean sorting chronology sequence for months
month_sales = df.groupby(month_col)[sales_col].sum()
axes[1].plot(month_sales.index, month_sales.values, marker="o", color="#2ca02c", linewidth=2.5)
axes[1].set_title("2. Monthly Revenue Growth Trend", fontsize=12, fontweight="bold")
axes[1].set_ylabel("Sales (₹)")
axes[1].grid(True, linestyle="--", alpha=0.5)

# --- CHART 3: Pie Chart (Profit Share Distribution) ---
cat_profit = df.groupby(category_col)[profit_col].sum().clip(lower=0) # clip handles negative values safely
axes[2].pie(cat_profit.values, labels=cat_profit.index, autopct='%1.1f%%', startangle=140, colors=['#ff7f0e', '#d62728', '#9467bd', '#8c564b'])
axes[2].set_title("3. Profit Share Distribution by Category", fontsize=12, fontweight="bold")

# --- CHART 4: Scatter Plot (Sales Amount vs. Profit Margins per Order) ---
axes[3].scatter(df[sales_col], df[profit_col], color="#e377c2", alpha=0.7, edgecolor="black")
axes[3].set_title("4. Correlation: Order Value vs. Profit Return", fontsize=12, fontweight="bold")
axes[3].set_xlabel("Order Value (₹)")
axes[3].set_ylabel("Profit earned (₹)")
axes[3].grid(True, linestyle="--", alpha=0.5)

# --- CHART 5: Horizontal Bar Chart (Top Performing Products) ---
top_products = df.groupby(product_col)[sales_col].sum().sort_values(ascending=True).tail(5)
top_products.plot(kind="barh", color="#17becf", edgecolor="black", ax=axes[4])
axes[4].set_title("5. Top 5 Best Selling Inventory Items", fontsize=12, fontweight="bold")
axes[4].set_xlabel("Revenue (₹)")
axes[4].grid(axis="x", linestyle="--", alpha=0.5)

# --- Empty Slot Cleanup ---
# Turn off the last unused layout square block in our 3x2 canvas area
axes[5].axis('off')

# Save configurations and render window layout safely
plt.tight_layout()
output_file = os.path.join("visualizations", "advanced_ecommerce_analysis.png")
plt.savefig(output_file, dpi=300)
print(f"💾 Success! Chart summary saved directly to: '{output_file}'")
plt.show()