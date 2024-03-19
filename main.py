from collections import Counter

BOOKPATH = 'books/frankenstein.txt'


def get_txt(f_path):
    with open(f_path) as f:

        return f.read()


def get_w_count(txt):
    words = txt.split()

    return len(words)


def get_l_count(txt):
    txt_lower = txt.lower()
    cnt = Counter()
    for l in txt_lower:
        cnt[l] += 1

    return dict(sorted(cnt.items()))


def print_report(w_c, l_c):
    print(f'--- Begin report of {BOOKPATH} ---')
    print(f'{w_c} words were found in the book')

    for l in l_c.keys():
        if l.isalpha() == True:
            print(f'The \'{l}\' character was found {l_c[l]} times.')

    print('--- End report ---')


def main():
    txt = get_txt(BOOKPATH)
    w_count = get_w_count(txt)
    l_count = get_l_count(txt)
    print_report(w_count, l_count)


main()