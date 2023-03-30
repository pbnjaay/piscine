import re

code_to_func = {
    '(bin)': lambda s: str(int(s, 2)),
    '(cap)': str.capitalize,
    '(hex)': lambda s: str(int(s, 16)),
    '(low)': str.lower,
    '(up)': str.upper,
}

def is_punctuation(word):
    pattern = r'^[.!,?:;]+$'
    match = re.search(pattern, word)
    return bool(match)


def should_replace_a_with_an(current_word, next_word):
    vowels = 'aeiou'
    if next_word and current_word:
        return current_word.lower() == 'a' and next_word[0].lower() in vowels
    return False
    

def is_matching(word):
    pattern = r'\((cap|low|up),\s*\d+\)'
    return bool(re.search(pattern, word))

def split_text(text:str):
    pattern = r'\([^)]+\)'
    matches = re.findall(pattern, text)

    for match in matches:
        text = text.replace(match, match.replace(' ', '_'))

    words = text.split()
    words = [word.replace('_', ' ') for word in words]

    return words

def split_punctuation_and_word(text:str):
    pattern = r'([.!,?:;]+)(\w+)'
    matches = re.findall(pattern, text)

    for match in matches:
        punct, word = match
        text = text.replace(punct+word, ' '.join([punct,word]))

    return text

def strip_espace_between_apostrophe_and_word(text: str):
    pattern = r''


def edit_text(text: str):
    i = 0
    text = split_punctuation_and_word(text)
    words = split_text(text)
    apostrophe_count = 0

    while i < len(words):
        current_word = words[i]
        next_word = words[i+1] if i+1 < len(words) else None
        prev_word = words[i-1] if i > 0 else None

        if current_word in code_to_func and prev_word:
            func = code_to_func[current_word]
            words[i-1] = func(prev_word)
            words.pop(i)
            i-=1    

        if is_matching(current_word):
            codes = current_word[1:-1].split(',')
            code = f'({codes[0]})'
            func = code_to_func[code]
            words.pop(i)
            i-=1
            n = int(codes[1]) if int(codes[1]) < i else i + 1
            for j in range(n):
                words[i-j] = func(words[i-j])

        if should_replace_a_with_an(current_word, next_word):
            words[i] = current_word + 'n'

        if is_punctuation(current_word) and prev_word:
            words[i-1] = prev_word + current_word
            words.pop(i)
            i-=1

        if current_word == "'" or current_word.startswith("'"):
            apostrophe_count +=1
            if apostrophe_count%2 == 0 and len(current_word) == 1 and prev_word:
                words[i-1] =  prev_word + current_word
                words.pop(i)
                i-=1
            else:
                if apostrophe_count%2 !=0 and len(current_word) == 1 and next_word:
                    words[i+1] = current_word + next_word
                    words.pop(i)
                    i+=1

        i +=1

    return ' '.join(words)


def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        content_file = input_file.read()

    edited_text = edit_text(content_file)

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(edited_text)

if __name__=='__main__':
    process_file('sample.txt', 'result.txt')