
🧾 pybudget
pybudget is an application for planning and analyzing personal budgets.

🚀 Features
✅ Add, delete, and edit income and expense entries

📊 Expense analysis: filtering, statistics by period, comparison with past periods

🎯 Set financial limits and goals

🧪 Test coverage (unit, integration, functional)

🖥️ CLI interface for budget interaction

📦 Optional documentation with Sphinx

🔧 Compliant with PEP 8 and PEP 257

📦 Installation and Setup

1. Clone the repository

git clone https://github.com/yourusername/pybudget.git
cd pybudget

2. Create and activate a virtual environment

python -m venv venv
.\venv\Scripts\Activate.ps1     # For PowerShell
# Or: .\venv\Scripts\activate.bat  # For CMD

3. Install dependencies

python -m pip install -r requirements.txt

4. Install the project in development mode

python -m pip install -e .

🧪 Running Tests
To run all tests using tox:

python -m tox

⚠️ Python 3.8 is used by default. Make sure it's installed on your system, or adjust tox.ini accordingly.

🖥️ CLI GUI Usage

cli
python -m pybudget.cli

commands

python -m pybudget.cli add-income --amount 80000 --category "Salary"                               
python -m pybudget.cli add-expense --amount 1500 --category "Groceries"                           
python -m pybudget.cli set-limit --category "Groceries" --amount 5000                            
python -m pybudget.cli show-stats --period month


gui
python -m pybudget.gui

🛠️ Development

Generate documentation with Sphinx
cd docs
make html
