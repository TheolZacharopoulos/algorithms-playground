def winner(andrea, maria, s):
    a_len = len(andrea)
    m_len = len(maria)

    a_sum = 0
    m_sum = 0

    for i in range(0, min(a_len, m_len)):
        if s == "Even" and i % 2 == 0:
            a_sum += andrea[i] - maria[i]
            m_sum += maria[i] - andrea[i]

        elif s == "Odd" and i % 2 != 0:
            a_sum += andrea[i] - maria[i]
            m_sum += maria[i] - andrea[i]

    if a_sum > m_sum:
        return "Andrea"
    elif m_sum > a_sum:
        return "Maria"
    else:
        return "Tie"


if __name__ == '__main__':
    a = [1, 1]
    m = [1, 1]
    # s = "Odd"
    s = "Even"

    print(winner(a, m, s))
