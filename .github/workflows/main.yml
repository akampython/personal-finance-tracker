name: Finance Tracker Workflow

on:
  workflow_dispatch:  # Allows manual triggering

jobs:
  filter_and_visualize:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pandas matplotlib openpyxl

      - name: Run the filter and visualize script
        run: python src/filter_and_visualize.py ${{ github.event.inputs.month }}

      - name: Upload Income and Expenses Summary Chart
        uses: actions/upload-artifact@v3
        with:
          name: income_expenses_summary
          path: output/income_expenses_summary.png

      - name: Upload Expenses by Category Pie Chart
        uses: actions/upload-artifact@v3
        with:
          name: expenses_by_category
          path: output/expenses_by_category.png
