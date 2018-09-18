def selection_sort(a):

    if not isinstance(a, list) or len(a) < 1:
        return a

    l = len(a)

    for i in range(l):
        global_min_index = i
        for j in range(i + 1, l):
            if a[j] < a[global_min_index]:
                global_min_index = j

        a[i], a[global_min_index] = a[global_min_index], a[i]

    return a
