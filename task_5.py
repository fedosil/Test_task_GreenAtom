def version_comparison(a: str, b: str) -> -1 | 0 | 1:
    a_list, b_list = a.split('.'), b.split('.')
    len_a_list, len_b_list = len(a_list), len(b_list)
    for i in range(min(len_a_list, len_b_list)):
        if a_list[i] == b_list[i]:
            continue
        elif a_list[i] < b_list[i]:
            return -1
        else:
            return 1
    return 0 if len_a_list == len_b_list else [1, -1][len_a_list < len_b_list]
