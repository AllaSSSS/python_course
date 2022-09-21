# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import re

def remove_words_with_substring(sentence, substring):
    return re.sub(r"\s*[а-яА-Я\w]*" + substring + r"[а-яА-Я\w]*", "", sentence)

print(remove_words_with_substring("Мы неабв очень любим Питон     \n иабв Джавуабв!", "абв"))