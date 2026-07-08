def validation(number):
    number = number.strip()

    if number.startswith('+98') and len(number) == 13:
        return number

    elif number.startswith('98') and len(number) == 12:
        return '+' + number

    elif number.startswith('09') and len(number) == 11:
        return '+98' + number[1:]

    else:
        return 'invalid'


n = int(input())
for _ in range(n):
    string = input()
    print(validation(string))