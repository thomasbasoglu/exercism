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
        for i in range(len(word)):
            if word[i] in vowels or (i > 0 and word[i] == "y"):
                if word[i] == "u" and i > 0 and word[i - 1] == "q":
                    split_idx = i + 1
                else:
                    split_idx = i
                break
        result.append(word[split_idx:] + word[:split_idx] + "ay")

    return " ".join(result)