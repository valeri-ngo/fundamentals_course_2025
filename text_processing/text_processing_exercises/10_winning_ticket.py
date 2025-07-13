def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return 'invalid ticket'
    winning_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_symbols in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uninterrupted_symbols
            if winning_symbol_repetition in left_part and \
                winning_symbol_repetition in right_part:
                if uninterrupted_symbols == 10:
                    return f'ticket "{ticket}" - {uninterrupted_symbols}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_symbols}{match_symbol}'
    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(', ')]

for ticket in tickets:
    print(check_ticket(ticket))