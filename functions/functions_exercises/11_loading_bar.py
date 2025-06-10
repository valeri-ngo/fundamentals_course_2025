def loading_dock(percent:int) -> str:
    loading_percents = percent // 10
    dots = 10 - loading_percents

    loading_bar = '[' + '%' * loading_percents + '.' * dots + ']'

    if percent == 100:
        return '100% Complete!\n' + loading_bar
    else:
        return(f'{percent}% {loading_bar}\nStill loading...')

current_input = int(input())
print(loading_dock(current_input))
