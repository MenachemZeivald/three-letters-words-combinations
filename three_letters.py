import csv

alphabet = "אבגדהוזחטיכלמנסעפצקרשת"
words_list = []


def csv_to_lst():
    with open("hebrew_words_three_letters.csv", encoding="utf-8-sig") as words_file:
        file = csv.reader(words_file)
        for line in file:
            words_list.append(line[0])


def word_checker():
    with open("letters.csv", "w", encoding="utf-8-sig", newline="") as letters_file:
        writer = csv.writer(letters_file)
        writer.writerow(["word", "count", "words"])
        already_in = []
        for a in alphabet:
            for b in alphabet:
                for c in alphabet:
                    count = 0
                    situation = []
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
                            situation.append(n)
                    if count > 4:
                        writer.writerow([a + b + c, count, situation])

    return True


csv_to_lst()
word_checker()
