def count_rearrangements(words):
    word_count = {}
    original_forms = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_count:
            word_count[sorted_word] += 1
        else:
            word_count[sorted_word] = 1

        if sorted_word not in original_forms:
            original_forms[sorted_word] = word

    for sorted_word, count in word_count.items():
        print(f"{original_forms[sorted_word]} = {count}")

words = ["python", "pyth", "ythopn", "thonpy", "nph", "thonp", "nothyp", "thy", "on", "no"]
count_rearrangements(words)
