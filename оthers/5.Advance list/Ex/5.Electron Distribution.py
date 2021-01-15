electrons = int(input())
final_list = []
shell = 1

while electrons > 0:
    max_elec_shell = 2 * shell ** 2
    if max_elec_shell > electrons:
        final_list.append(electrons)
        break
    else:
        final_list.append(max_elec_shell)
    electrons -= max_elec_shell
    shell += 1

print(final_list)
