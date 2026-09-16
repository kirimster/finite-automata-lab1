# ============================================================
# ЧАСТЬ 1. ДКА для задачи "а"
# ============================================================

# ---------- Табличное представление ДКА ----------
# Состояния
Q0, Q1, Q2, Q3, Q4 = 0, 1, 2, 3, 4

DFA_STATE_NAMES = {
    Q0: "q0",
    Q1: "q1",
    Q2: "q2",
    Q3: "q3",
    Q4: "q4"
}

# Алфавит
DFA_ALPHABET = ['0', '1']

# Таблица переходов: DFA_TRANS[состояние][индекс_символа] = новое состояние
DFA_TRANS = [
    [Q1, Q0],  # q0: 0->q1, 1->q0
    [Q2, Q4],  # q1: 0->q2, 1->q0
    [Q3, Q0],  # q2: 0->q2, 1->q3
    [Q3, Q4],  # q3: 0->q3, 1->q3
    [Q4, Q4]   # q4 : 0->q4, 1->q4
]

# Финальные состояния
DFA_FINAL = {Q0, Q1, Q2, Q3}

# Начальное состояние
DFA_START = Q0


def dfa_process(input_string):
    """Обрабатывает строку на ДКА. Возвращает True/False/None."""
    current = DFA_START
    print(f"  Начальное состояние: {DFA_STATE_NAMES[current]}")

    for ch in input_string:
        # Проверка символа
        pos = -1
        for i in range(len(DFA_ALPHABET)):
            if DFA_ALPHABET[i] == ch:
                pos = i
                break
        if pos == -1:
            print(f"  Ошибка: неизвестный символ '{ch}'")
            return None

        current = DFA_TRANS[current][pos]
        print(f"  Прочитан '{ch}' -> {DFA_STATE_NAMES[current]}")

    if current in DFA_FINAL:
        print("  Результат: Accepted")
        return True
    else:
        print("  Результат: Rejected")
        return False


# ============================================================
# ЧАСТЬ 2. НКА для задачи "б"
# ============================================================

# ---------- Табличное представление НКА ----------
NQ0, NA0, NA1, NA2, NA3, NQF = 0, 1, 2, 3, 4, 5

NFA_STATE_NAMES = {
    NQ0: "Q0",
    NA0: "A0",
    NA1: "A1",
    NA2: "A2",
    NA3: "A3",
    NQF: "QF"
}

NFA_ALPHABET = ['0', '1']

# Таблица переходов: NFA_TRANS[состояние][индекс] = множество состояний
NFA_TRANS = [
    [{NQ0, NA0}, {NQ0}],   # Q0: 0->{Q0,A0}, 1->{Q0}
    [{NQF},      {NA1}],   # A0: 0->{QF},    1->{A1}
    [{NA2},      {NA2}],   # A1: 0->{A2},    1->{A2}
    [{NA3},      {NA3}],   # A2: 0->{A3},    1->{A3}
    [{NA0},      {NA0}],   # A3: 0->{A0},    1->{A0}
    [{NQF},      {NQF}],   # QF: 0->{QF},    1->{QF}
]

NFA_FINAL = {NQF}
NFA_START = NQ0


def nfa_process(input_string):
    """Обрабатывает строку на НКА. Возвращает True/False/None."""
    current_set = {NFA_START}
    print(f"  Начальное множество: {{ {NFA_STATE_NAMES[NFA_START]} }}")

    for ch in input_string:
        pos = -1
        for i in range(len(NFA_ALPHABET)):
            if NFA_ALPHABET[i] == ch:
                pos = i
                break
        if pos == -1:
            print(f"  Ошибка: неизвестный символ '{ch}'")
            return None

        next_set = set()
        for state in current_set:
            next_set.update(NFA_TRANS[state][pos])

        current_set = next_set

        if not current_set:
            print("  Результат: Rejected (нет достижимых состояний)")
            return False

        names = sorted(NFA_STATE_NAMES[s] for s in current_set)
        print(f"  Прочитан '{ch}' -> {{ {', '.join(names)} }}")

    if current_set & NFA_FINAL:
        print("  Результат: Accepted")
        return True
    else:
        print("  Результат: Rejected")
        return False


# ============================================================
# MAIN
# ============================================================

def main():
    print("Практическая работа №1. Конечные автоматы")
    print("Выберите автомат:")
    print("  1 - ДКА (содержит подстроку '001')")
    print("  2 - НКА (два нуля на расстоянии, кратном 4)")

    choice = input("Ваш выбор (1 или 2): ").strip()

    if choice == '1':
        print("\n=== ДКА: содержит подстроку '001' ===")
        print("(введите пустую строку для выхода)")
        while True:
            s = input("Строка: ")
            if s == "":
                break
            dfa_process(s)
            print()
    elif choice == '2':
        print("\n=== НКА: два нуля на расстоянии, кратном 4 ===")
        print("(введите пустую строку для выхода)")
        while True:
            s = input("Строка: ")
            if s == "":
                break
            nfa_process(s)
            print()
    else:
        print("Неверный выбор.")


if __name__ == "__main__":
    main()