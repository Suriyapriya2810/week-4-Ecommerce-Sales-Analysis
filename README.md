

**🛒 E-Commerce Sales Analysis**

Welcome to the E-Commerce Sales Analysis project! This is the complete submission for the Week 4 Capstone Project (Option 4) for The Developers Arena Data Science Internship.

📋 Project Overview

The goal of this project is to take a raw sales dataset (sales_data.csv) and build an automated Python program to clean the data, calculate important business metrics (KPIs), and create visual charts.

This helps an e-commerce business easily understand its total revenue, profits, and customer shopping trends.

**Key Objectives:**

Clean Data Automatically: Fix formatting errors and remove invalid rows without crashing.

Calculate Business Metrics: Find Total Revenue, Total Profit, Average Order Value (AOV), and Net Profit Margin.

Create 5 Charts: Build a visual dashboard using matplotlib to see sales trends, best-selling products, and profit breakdowns.

**📂 Project Structure**

To match the internship folder requirements, the repository is organized exactly like this:

Plaintext
Ecommerce-Sales-Analysis/
│
├── data/
│   └── sales_data.csv                    # Raw sales dataset from the dashboard
│
├── visualizations/
│   └── advanced_ecommerce_analysis.png   # Auto-generated 5-chart visual dashboard
│
├── report/
│   └── project_report.docx               # Your final Microsoft Word report documentation
│
├── main.py                               # The clean, error-free Python pipeline code
├── requirements.txt                      # List of required external python libraries
└── README.md                             # This overview documentation file

🛠️ Setup & Installation Instructions
Follow these steps to run the project on your local computer:

Step 1: Open Terminal / Command Prompt
Open your terminal application (Command Prompt on Windows or Terminal on Mac).

Step 2: Navigate to Your Project Folder
Go into your active week 4 project directory:

Bash
cd C:\Users\HP\OneDrive\Desktop\Ecommerce-Sales-Analysis\4
Step 3: Install Required Libraries
Install the official Python packages needed to run the data analysis and chart generation:

Bash
pip install pandas matplotlib
Step 4: Run the Python Script
Run the main code file to process the data and generate your charts:

Bash
python main.py
📊 Key Insights Found
When the script runs successfully, it calculates the following key business indicators from your data:

Total Revenue Generated: The total amount of money made from all e-commerce sales.

Total Net Profit Earned: The actual money kept after costs are deducted.

Average Order Value (AOV): The average amount of money spent by a customer per transaction.

Net Profit Margin (%): The efficiency percentage of how well sales are converted into actual profits.

**📈 Visual Dashboard Details**

The script automatically saves a single high-resolution image (advanced_ecommerce_analysis.png) inside the visualizations/ folder containing 5 different charts:

Bar Chart: Revenue contribution grouped by product department.

Line Chart: Chronological sales trend showing performance over the months.

Pie Chart: Proportional profit share distribution per category.

Scatter Plot: Correlation matching individual order sizes against their profit return.

Horizontal Bar Chart: Standout ranking of the Top 5 best-selling individual inventory items.

📝 Technologies Used

Language: Python

Data Manipulation: Pandas

Data Visualization: Matplotlib
