r"""Четвертое задание.

Вы - начинающий журналист. Накануне вечером вы написали статью про кошек для
ветеринарного журнала, но забыли заблокировать компьютер. На утро вы
обнаружили, что вашей собаке не понравилось, что пишете вы про кошек, а не про
собак. Она испортила вам статью, и оставила следующую записку:
1) я заменила все слова "cat" в статье на "woof-woof"
2) я развернула каждое предложение и добавила в его конец, перед точкой,
строку, состояющую из символа "!". Длина этой строки восклицательных знаков
равна длине предложения (без учета точки).
3) я перевела все предложения в верхний регистр

Попробуй вернуть все назад, woof-woof!

Ваша задача вернуть текст в первозданный вид.
Ограничения:
1) В результате предложения разделены символом '.\n'.
2) В результате все предложения начинаются с буквы верхнего регистра. Это
единственная буква в верхнем регистре в предложении.

Исходный текст представлен в файле correct_article.txt.
Испорченный текст представлен в файле wrong_article.txt.

Реализуйте код, который восстановит статью и вернет ее в качестве результата
работы функции.

Проверка результата:
pytest ./4_safe_text/test.py
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    """Функция для чтения статьи в виде строки.

    Args:
        path: путь до статьи

    Returns:
        Текст статьи в виде строки
    """
    with open(path, 'r') as file_article:
        article = file_article.read()
    return article


def get_correct_article() -> str:
    """Функция возвращает корректную статью в виде строки.

    Returns:
        Корректная статья в виде строки
    """
    return get_article(
        os.path.join(
            BASE_DIR,
            '4_safe_text',
            'articles',
            'correct_article.txt',
        ),
    )


def get_wrong_article() -> str:
    """Функция возвращает испорченную статью в виде строки.

    Returns:
        Испорченная статья в виде строки
    """
    return get_article(
        os.path.join(
            BASE_DIR,
            '4_safe_text',
            'articles',
            'wrong_article.txt',
        ),
    )


def corrected(wrong_article_lines: list) -> str:
    """Итератор обработки предложений.

    Args:
        wrong_article_lines: список испорченный предложений

    Yields:
        Исправленное предложение
    """
    for sentence in wrong_article_lines:
        sentence = sentence.strip('!')
        sentence = sentence[::-1]
        sentence = re.sub('WOOF-WOOF', 'CAT', sentence)
        yield sentence.capitalize()


def recover_article() -> str:
    """Функция возвращает восстановленную статью в виде строки.

    Returns:
        Восстановленная статья в виде строки.
    """
    wrong_article = get_wrong_article()
    return SPLIT_SYMBOL.join(corrected(wrong_article.split(SPLIT_SYMBOL)))
