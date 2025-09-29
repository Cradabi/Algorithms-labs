def knapsack(w, v, c):
    n = len(w)
    memo = {}

    def dp(i, cap):
        if i == 0 or cap == 0:
            return 0
        if (i, cap) in memo:
            return memo[(i, cap)]

        if w[i - 1] > cap:
            res = dp(i - 1, cap)
        else:
            res = max(
                dp(i - 1, cap),
                v[i - 1] + dp(i - 1, cap - w[i - 1])
            )
        memo[(i, cap)] = res
        return res

    def restore_items():
        taken = []
        i, cap = n, c
        while i > 0 and cap > 0:
            if dp(i, cap) != dp(i - 1, cap):
                taken.append(i - 1)
                cap -= w[i - 1]
            i -= 1
        return taken

    max_value = dp(n, c)
    taken_items = restore_items()
    return max_value, taken_items

def simulate_heist(w, v, scap, howm, runs):
    w = w.copy()
    v = v.copy()

    total_stolen = 0
    total_value = 0
    all_taken = []

    for attempt in range(runs):
        if total_stolen >= howm:
            break

        # Собираем доступные предметы
        valid_w = []
        valid_v = []
        index_map = []

        for i in range(len(w)):
            if w[i] != -1:
                valid_w.append(w[i])
                valid_v.append(v[i])
                index_map.append(i)

        if not valid_w:
            break

        value, taken = knapsack(valid_w, valid_v, scap)

        if not taken:
            break  # ничего не удалось взять

        real_taken = [index_map[i] for i in taken]

        for i in real_taken:
            w[i] = -1
            v[i] = -1

        total_stolen += len(real_taken)
        total_value += value
        all_taken.append(real_taken)

    return {
        "success": total_stolen >= howm,
        "total_items_stolen": total_stolen,
        "total_value_stolen": total_value,
        "rounds": len(all_taken),
        "items_per_round": all_taken
    }


if __name__ == "__main__":
    w = [1, 55, 4, 3, 2, 1]
    v = [1, 100, 10, 35, 4, 10]
    scap = 10
    howm = 6
    runs = 3

    res = simulate_heist(w, v, scap, howm, runs)

    print("Успешно:", res["success"])
    print("Количество украденных предметов:", res["total_items_stolen"])
    print("Общая ценность:", res["total_value_stolen"])
    print("Количество заходов:", res["rounds"])
    print("Предметы по заходам:", res["items_per_round"])