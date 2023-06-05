def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def longest_collatz_sequence(limit):
    max_length = 0
    max_start = 0
    step = [0] * (limit + 1)
    for i in range(1, limit + 1):
        if step[i] != 0:
            continue
        sequence = collatz_sequence(i)
        length = len(sequence)
        for j, num in enumerate(sequence):
            if num <= limit:
                if step[num] == 0:
                    step[num] = length - j + step[i]
                else:
                    break
        if step[i] > max_length:
            max_length = step[i]
            max_start = i
    return max_start


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = longest_collatz_sequence(n)
        print(result)
