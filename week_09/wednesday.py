try:
    with open('does_not_exist') as f:
        text = f.read()
    print('text=', text)
except FileNotFoundError:
    print("oops")