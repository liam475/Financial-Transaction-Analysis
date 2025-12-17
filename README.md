# Financial Transaction Analysis System

A Python-based financial transaction analysis system for storing, analyzing, and visualizing transaction-level financial data.

## Overview
This application allows users to record financial transactions, import bulk data from CSV files, and generate analytical summaries and visualizations.  
It is built with a modular design that separates application control, database management, analytical logic, and data visualization.

The project emphasizes clean data handling, SQL-based aggregation, and analytical insights relevant to finance and data-driven decision making.

## Features
- Manual entry of financial transactions
- Bulk transaction import from CSV files
- Persistent data storage using SQLite
- Category-level spending and income analysis
- Monthly cashflow analysis
- Data visualization with bar charts and time-series plots

## Technologies Used
- Python
- SQLite
- SQL
- matplotlib

## Project Structure
- app.py - Application controller and menu system
- db.py - Database creation and data access logic
- analysis.py - SQL-based analytical queries
- charts.py - Data visualization functions
- .gitignore - Excludes generated and local data files
## Usage Example
When the application is run, users interact with a menu-driven interface:
1. Add transaction
2. List transactions
3. Summary by category
4. Monthly cashflow
5. Category bar chart
6. Monthly net cashflow chart
7. Import transactions from CSV
8. Exit

-  Users can enter transactions manually, import bulk data from CSV files, and generate analytical summaries and visualizations directly from the menu.
