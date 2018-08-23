"""
주어진 유니코드 한글 문자열에서 특수문자, 띄어쓰기를 무시하며 특정 미완성 문자열을 찾고,
완성된 단어들을 찾기, 영어나 숫자는 무시
"""
import re
import hgtk


def find_keywords(input_text, target):

    result = []

    fixed_input_text = re.sub('[-=.#/?:$}~]', '', input_text)

    # 텍스트를 어절로 나눔
    words_list = fixed_input_text.split(' ')

    # 텍스트의 문자들을 초/중/종성으로 분리
    disassembled_text = hgtk.text.decompose(fixed_input_text)

    # 분리된 문자들의 구분자(ᴥ)를 제거
    remove_composer_code_in_disassembled_text = disassembled_text.replace('ᴥ', '')

    # 구분자(ᴥ)가 제거된 분리된 텍스트를 어절로 나눔
    disassembled_word_list = remove_composer_code_in_disassembled_text.split(' ')

    # 찾는 문자열의 공백과 특수 문자 제거
    fixed_target = re.sub('[-=.#/?:$}\s]', '', target)

    # 찾는 문자열 분해
    disassembled_target_text = hgtk.text.decompose(fixed_target)

    # 분리된 문자들의 구분자(ᴥ)를 제거
    remove_composer_code_in_disassembled_target_text = disassembled_target_text.replace('ᴥ', '')

    # 초성 하나만 넣었을 경우
    if len(remove_composer_code_in_disassembled_target_text) == 1:
        for word in disassembled_word_list:
            if word[0] == remove_composer_code_in_disassembled_target_text[0]:
                result.append(words_list[disassembled_word_list.index(word)])
    else:
        for word in disassembled_word_list:
            if remove_composer_code_in_disassembled_target_text in word:
                result.append(words_list[disassembled_word_list.index(word)])

    return result
