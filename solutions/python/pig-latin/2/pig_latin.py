"""This program translates Pig Latin"""
def translate(text):
    """This is the only function so guess what this does """
    vowels = "aeiou"
    result = []

    for word in text.split():
        if word.startswith(tuple(vowels)) or word.startswith(("xr", "yt")):
            result.append(word + "ay")
            continue

        split_idx = 0
        for index in range(len(word)):
            if word[index] in vowels or (index > 0 and word[index] == "y"):
                if word[index] == "u" and index > 0 and word[index - 1] == "q":
                    split_idx = index + 1
                else:
                    split_idx = index
                break
        result.append(word[split_idx:] + word[:split_idx] + "ay")

    return " ".join(result)