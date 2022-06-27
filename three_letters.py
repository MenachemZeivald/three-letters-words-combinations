import csv
from timeit import default_timer

alphabet = "אבגדהוזחטיכלמנסעפצקרשת"
words_list = {}


def word_checker():
    with open("hebrew_words_three_letters.csv", encoding="utf-8-sig") as words_file:
        file = csv.reader(words_file)
        for line in file:
            words_list[line[0]] = int(line[1])
    with open("letters.csv", "w", encoding="utf-8-sig", newline="") as letters_file:
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


start = default_timer()
word_checker()
end = default_timer()
print(f"the time is {end-start}")
