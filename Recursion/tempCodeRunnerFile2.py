def segment(text, language, data, index):
    # print(data)
    if data != "" and len(data) <= len(text) and data[-1] != text[len(data) - 1]:
        return False

    if len(data) > len(text):
        return False

    if index >= len(language):
        return False

    if data == text:
        return True

    return segment(text, language, data + language[index], 0) or segment(text, language, data, index + 1)


def get_language(arr):
    if len(arr) == 1:
        return [arr[0].strip("'")]

    return [arr[0].strip("'")] + get_language(arr[1:])


print("Enter list[str]: ", end="")
inp = input().split(", ")
inp = get_language(inp)

str = inp[0]
lang = inp[1:]

print(f"text: str = '{str}'")
print(f"lang: list[str] = {lang}")
print(f"segment(text, lang) -> {segment(str, lang, '', 0)}")
