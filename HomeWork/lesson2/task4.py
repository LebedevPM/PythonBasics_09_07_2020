user_str = input('Введите какое-нибудь предложение')
user_str = user_str.split()
print(user_str)
i = 0
while i < len(user_str):
    if len(user_str[i]) > 10:
        print(f'{i + 1:>2}. {user_str[i][:10]}')
    else:
        print(f'{i + 1:>2}. {user_str[i]:<10}')
    i += 1
