# test_budget_manager.py
import subprocess
import sys


def run_cli(args):
    """Запускает CLI-команду и возвращает вывод."""
    result = subprocess.run(
        [sys.executable, "-m", "pybudget.cli"] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8", errors="replace")


def test_add_income_valid():
    output = run_cli(["add-income", "--amount", "80000", "--category", "Salary"])
    assert "Доход добавлен" in output
    assert "80000" in output
    assert "Salary" in output


def test_add_expense_valid():
    output = run_cli(["add-expense", "--amount", "1500", "--category", "Groceries"])
    assert "Расход добавлен" in output
    assert "1500" in output
    assert "Groceries" in output


def test_set_limit_valid():
    output = run_cli(["set-limit", "--category", "Groceries", "--amount", "5000"])
    assert "Лимит установлен" in output
    assert "5000" in output
    assert "Groceries" in output


def test_show_stats_month():
    output = run_cli(["show-stats", "--period", "month"])
    assert "Показ статистики" in output
    assert "month" in output


def test_show_stats_week():
    output = run_cli(["show-stats", "--period", "week"])
    assert "Показ статистики" in output
    assert "week" in output


def test_show_stats_default():
    output = run_cli(["show-stats"])
    assert "Показ статистики" in output
    assert "month" in output  # по умолчанию


def test_add_income_missing_amount():
    result = subprocess.run(
        [sys.executable, "-m", "pybudget.cli", "add-income", "--category", "Bonus"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    assert "error" in result.stderr.decode("utf-8", errors="replace")


def test_add_expense_missing_category():
    result = subprocess.run(
        [sys.executable, "-m", "pybudget.cli", "add-expense", "--amount", "1000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    assert "error" in result.stderr.decode("utf-8", errors="replace")


def test_set_limit_negative():
    output = run_cli(["set-limit", "--category", "Games", "--amount", "-1000"])
    assert "Лимит установлен" in output  # CLI не обрабатывает отрицательные, но тест покрывает


def test_help_message():
    result = subprocess.run(
        [sys.executable, "-m", "pybudget.cli"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    output = result.stdout.decode("utf-8", errors="replace")
    assert "Доступные команды" in output
