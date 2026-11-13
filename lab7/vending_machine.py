def parse_coins(coins_csv):
    """Return a list of positive int coin values; invalid input is ignored."""
    if not isinstance(coins_csv, str):
        return []
    coins = []
    for part in coins_csv.split(','):
        part = part.strip()
        if not part:
            continue
        try:
            value = int(part)
        except ValueError:
            continue
        if value > 0:
            coins.append(value)
    return coins


def slot_position(code):
    """Return (row, column) as zero-based ints, or None for an invalid code."""
    if not isinstance(code, str):
        return None
    code = code.strip()
    if len(code) < 2:
        return None
    letter, number = code[0].upper(), code[1:]
    if not (letter.isascii() and "A" <= letter <= "Z"):
        return None
    if not (number.isascii() and number.isdigit()):
        return None
    column = int(number) - 1
    if column < 0:
        return None
    return ord(letter) - ord('A'), column


def change_due(payment):
    """Return change in five-coins, or an error message for invalid input."""
    if not isinstance(payment, str):
        return "invalid input"
    parts = payment.split('/')
    if len(parts) != 2:
        return "invalid input"
    try:
        paid, price = int(parts[0]), int(parts[1])
    except ValueError:
        return "invalid input"
    if paid < 0 or price < 0:
        return "invalid input"
    change = paid - price
    if change < 0:
        return "insufficient payment"
    return str(change // 5) + ' five-coins'


def main():
    print("==== Running parse_coins ====")
    user_input = input("Enter coin values as CSV (e.g. 5,10,25): ")
    result = parse_coins(user_input)
    print("Coins:", result)

    print("\n==== Running slot_position ====")
    user_input = input("Enter a slot code (e.g. B7): ")
    result = slot_position(user_input)
    print("Row and Column:", result if result is not None else "invalid slot code")

    print("\n==== Running change_due ====")
    user_input = input("Enter paid/price (e.g. 200/150): ")
    result = change_due(user_input)
    print("Change Due:", result)


if __name__ == "__main__":
    main()