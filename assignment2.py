class Palindrome:
    def __init__(self, name: str):
        self.name = name

    def check_palindrome(self) -> bool:
        cleaned = self.name.replace(" ", "").lower()
        return cleaned == cleaned[::-1]

word = Palindrome("Racecar")
print(word.check_palindrome())
