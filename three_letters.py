import csv
from timeit import default_timer

alphabet = "אבגדהוזחטיכלמנסעפצקרשת"


def word_checker():
    words_list = {}
    with open("words_with_three_letters.csv", encoding="utf-8-sig") as words_file:
        file = csv.reader(words_file)
        for line in file:
            words_list[line[0]] = int(line[1])
    with open(
        "first_solution.csv", "w", encoding="utf-8-sig", newline=""
    ) as letters_file:
        writer = csv.writer(letters_file)
        writer.writerow(["word", "count", "words", "score", "sum", "average"])
        already_in = []
        for a in alphabet:
            for b in alphabet:
                for c in alphabet:
                    count = 0
                    situation = {}
                    num = [
                        a + b + c,
                        a + c + b,
                        b + a + c,
                        b + c + a,
                        c + a + b,
                        c + b + a,
                    ]
                    for n in num:
                        if n in words_list and n not in already_in:
                            count += 1
                            already_in.append(n)
                            situation[n] = words_list[n]
                    if count > 4:
                        writer.writerow(
                            [
                                a + b + c,
                                count,
                                ", ".join([i for i in situation]),
                                ", ".join([str(i) for i in situation.values()]),
                                sum(situation.values()),
                                (sum(situation.values())) // 6,
                            ]
                        )

    return True


def second_solution():
    words_list = []
    words_count = {}
    with open("words_with_three_letters.csv", encoding="utf-8-sig") as words_file:
        file = csv.reader(words_file)
        for line in file:
            words_list.append("".join(sorted(list(line[0]))))
    for word in words_list:
        try:
            words_count[word] += 1
        except KeyError:
            words_count[word] = 1
    with open(
        "second_solution.csv", "w", encoding="utf-8-sig", newline=""
    ) as letters_file:
        writer = csv.writer(letters_file)
        writer.writerow(["word", "count"])
        for word in words_count:
            writer.writerow([word, words_count[word]])


start = default_timer()
word_checker()
end = default_timer()
print(f"the time is {end-start}")


start = default_timer()
second_solution()
end = default_timer()
print(f"the time is {end-start}")
