import re

def read_input(file):
    with open(file) as f:
        lines = f.readlines()

    tokens = re.findall("(\w+)", lines[0])

    words = [line.strip() for line in lines[2:]]

    return tokens, words

def find_token_positions(word, token):
    positions = [False] * len(word)
    token_length = len(token)

    for i in range(len(word) - token_length + 1):
        if word[i:i + token_length] == token:
            for j in range(token_length):
                positions[i + j] = True

    return positions

def main():
    tokens, words = read_input("day19/input/input.txt")

    # Try big tokens first
    tokens = sorted(tokens, key=len)

    regex = '|'.join(tokens)
    print(regex)

    re_possibles = []
    possibles = []
    for word in words:
        matches = re.findall(regex, word)
        if ''.join(matches) == word:
            re_possibles.append(word)

        positions = [False] * len(word)
        for token in tokens :
            token_positions = find_token_positions(word, token)
            positions = [t or p for t, p in zip(token_positions, positions)]
        if all(positions):
            possibles.append(word)

    re_possibles = set(re_possibles)

    diff = []
    for p in possibles:
        if p not in re_possibles:
            print(p)
            diff.append(p)

    print(f"Part 1: {len(re_possibles)}")
    # Added my own tokens and a word. The tokens are uw wu and the word is ruwu.
    # It should not be possible to create ruwu, but my problem now is that it
    # thinks that this combination is possible.
    # 338 is to high
    # 309 is to low
    # 299 is to low



if __name__ == '__main__':
    main()
