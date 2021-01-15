def perfect_numb(n):
    numb_list = []
    for numb in range(1, n):
        if n % numb == 0:
            numb_list.append(numb)
    if n == sum(numb_list):
        return True
    return False


number = int(input())
if perfect_numb(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
