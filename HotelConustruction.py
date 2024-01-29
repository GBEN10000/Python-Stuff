def task_of_pairing(freq):
    no_of_pairs = 0
    remaining = 0

    for i in range(len(freq)):
        if freq[i] != 0:
            if remaining != 0:
                no_of_pairs += (freq[i] + remaining) // 2
            else:
                no_of_pairs += freq[i] // 2

            if (freq[i] + remaining) % 2 != 0:
                remaining = (freq[i] + remaining) % 2
            else:
                remaining = 0
        else:
            remaining = 0

    return no_of_pairs

if __name__ == "__main__":
    freq_count = int(input().strip())

    freq = [int(input().strip()) for _ in range(freq_count)]

    result = task_of_pairing(freq)

    print(result)
