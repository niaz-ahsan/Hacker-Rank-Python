import textwrap

def wrap(string, max_width):
    list = textwrap.wrap(string, max_width)
    return "\n".join(list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

    