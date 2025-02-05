"""Третье задание.

Вам дан список предложений. Предложения содержат только слова, которые
разделены единичными пробелами. Необходимо вернуть максимальное количество
слов, которое содержится в одном предложении. sentences[i] - это одно
предложение. Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    """Функция подсчета максимального количества слов в предложении.

    Args:
        sentences: список предложений.

    Returns:
        Максимальное кол-во слов в одном предложении.
    """
    return max(len(sentence.split()) for sentence in sentences)
