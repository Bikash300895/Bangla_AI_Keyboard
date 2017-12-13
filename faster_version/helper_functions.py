def load_user_history_word():
    import io
    file = io.open("data/user_words.txt", mode="r", encoding="utf-8")

    user_words_old = []
    
    for line in file:
        if line[-1] == '\n' or line[-1] == ' ':
            line = line[:-1
                   ]
        user_words_old.append(line.split(' ')[0])
        user_words_old = user_words_old[::-1]

    return user_words_old


def load_english_word():
    file = open('data/eng_word_count.txt')

    global eng_words
    eng_words = load_user_history_word()

    if 'user_words' in globals():
        global user_words
        eng_words.extend(user_words)

    for line in file:
        eng_words.append(line.split(" ")[0])


def english_word_search(start):
    if 'eng_words' not in globals():
        load_english_word()

    words_with_start = []
    for word in eng_words:
        if word.startswith(start):
            words_with_start.append(word)

            if len(words_with_start) == 7:
                return words_with_start

    for word in eng_words:
        if start in word:
            words_with_start.append(word)

            if len(words_with_start) == 7:
                return words_with_start

    return words_with_start


def load_bangla_word():
    import io
    file = io.open("data/bangla_word_freq_count.txt", mode="r", encoding="utf-8")

    global bangla_words
    bangla_words = load_user_history_word()

    if 'user_words' in globals():
        global user_words
        bangla_words.extend(user_words)

    for line in file:
        bangla_words.append(line.split(" ")[0])


def bangla_word_search(start):
    if 'bangla_words' not in globals():
        load_bangla_word()

    words_with_start = []
    for word in bangla_words:
        if word.startswith(start) and word != start:
            words_with_start.append(word[:-1])

            if len(words_with_start) == 7:
                return words_with_start
    for word in bangla_words:
        if start in word:
            words_with_start.append(word[:-1])

            if len(words_with_start) == 7:
                return words_with_start

    return words_with_start


def get_clipboard_data():
    import win32clipboard

    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData()
    except:
        data = None

    win32clipboard.CloseClipboard()

    return data


if __name__ == '__main__':
    print(english_word_search('kf'))
    print(bangla_word_search('ব'))
    print(get_clipboard_data())
    load_user_history_word()
