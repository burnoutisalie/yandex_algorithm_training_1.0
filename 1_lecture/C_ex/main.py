def get_digits_from_input(phone_input, phone_list):
    for char in phone_input:
        if char.isdigit():
            phone_list.append(char)

def bring_uniform_format(phone):
    if len(phone) == 11:
        phone.pop(0)
    elif len(phone) <= 8:
        if len(phone) == 8:
            phone.pop(0)
        phone.insert(0, '4')
        phone.insert(1, '9')
        phone.insert(2, '5')

def compare_numbers():
    phone_new = input()
    phone1 = input()
    phone2 = input()
    phone3 = input()
    phone_dir = [[], [], [], []]
    get_digits_from_input(phone_new, phone_dir[0])
    get_digits_from_input(phone1, phone_dir[1])
    get_digits_from_input(phone2, phone_dir[2])
    get_digits_from_input(phone3, phone_dir[3])
    for ph in phone_dir:
        bring_uniform_format(ph)
    for i in range(1, len(phone_dir)):
        if phone_dir[0] == phone_dir[i]:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    compare_numbers()
