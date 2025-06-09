# pybudget/cli.py

import argparse

def add_income(args):
    print(f"✅ Доход добавлен: {args.amount} руб, категория: {args.category}")

def add_expense(args):
    print(f"💸 Расход добавлен: {args.amount} руб, категория: {args.category}")

def show_stats(args):
    print(f"📊 Показ статистики за период: {args.period}")

def set_limit(args):
    print(f"🔒 Лимит установлен: {args.amount} руб на категорию {args.category}")

def main():
    parser = argparse.ArgumentParser(description="🧾 pybudget CLI")
    subparsers = parser.add_subparsers(title="Доступные команды")

    # Добавление дохода
    parser_income = subparsers.add_parser("add-income", help="Добавить доход")
    parser_income.add_argument("--amount", type=float, required=True)
    parser_income.add_argument("--category", required=True)
    parser_income.set_defaults(func=add_income)

    # Добавление расхода
    parser_expense = subparsers.add_parser("add-expense", help="Добавить расход")
    parser_expense.add_argument("--amount", type=float, required=True)
    parser_expense.add_argument("--category", required=True)
    parser_expense.set_defaults(func=add_expense)

    # Показать статистику
    parser_stats = subparsers.add_parser("show-stats", help="Показать статистику")
    parser_stats.add_argument("--period", choices=["day", "week", "month"], default="month")
    parser_stats.set_defaults(func=show_stats)

    # Установить лимит
    parser_limit = subparsers.add_parser("set-limit", help="Установить лимит")
    parser_limit.add_argument("--category", required=True)
    parser_limit.add_argument("--amount", type=float, required=True)
    parser_limit.set_defaults(func=set_limit)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
