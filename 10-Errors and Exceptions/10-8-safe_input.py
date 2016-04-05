def safe_input(msg):
    data = None
    try:
        data = raw_input(msg)
    except (EOFError, KeyboardInterrupt):
        pass
    return data

if __name__ == '__main__':
    print safe_input("please input: ")
