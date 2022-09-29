def IVA(any_number: int):
    foo = str(any_number)
    while len(foo) < 7:
        foo = foo + '0'
    if len(foo) > 7:
        foo = foo[:7]
    foo = foo + '017'  # Codice Ufficio IVA
    iva = foo
    control_char = 0 if ((int(iva[0]) + int(iva[2]) + int(iva[4]) + int(iva[6]) + int(iva[8])) + (
            (int(iva[1]) * 2 - 9 if int(iva[1]) * 2 > 9 else int(iva[1]) * 2) + (
        int(iva[3]) * 2 - 9 if int(iva[3]) * 2 > 9 else int(iva[3]) * 2 + 0) + (
                int(iva[5]) * 2 - 9 if int(iva[5]) * 2 > 9 else int(iva[5]) * 2 + 0) + (
                int(iva[7]) * 2 - 9 if int(iva[7]) * 2 > 9 else int(iva[7]) * 2 + 0) + (
                int(iva[9]) * 2 - 9 if int(iva[9]) * 2 > 9 else int(iva[9]) * 2))) % 10 == 0 else 10 - (
            (int(iva[0]) + int(iva[2]) + int(iva[4]) + int(iva[6]) + int(iva[8])) + (
            (int(iva[1]) * 2 - 9 if int(iva[1]) * 2 > 9 else int(iva[1]) * 2) + (
        int(iva[3]) * 2 - 9 if int(iva[3]) * 2 > 9 else int(iva[3]) * 2 + 0) + (
                int(iva[5]) * 2 - 9 if int(iva[5]) * 2 > 9 else int(iva[5]) * 2 + 0) + (
                int(iva[7]) * 2 - 9 if int(iva[7]) * 2 > 9 else int(iva[7]) * 2 + 0) + (
                int(iva[9]) * 2 - 9 if int(iva[9]) * 2 > 9 else int(iva[9]) * 2))) % 10
    return iva + str(control_char)


example_number = 2345674

print(IVA(example_number))
