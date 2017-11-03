def max_match(sentence, dictionary):
    """
    MaxMatch算法
    """

    if not sentence:
        return ''
    sentence_length = len(sentence)
    
    for length in range(sentence_length, 0, -1):
        firstword = sentence[0:length]
        remainder = sentence[length : ]
        # print(firstword, remainder)
        if firstword in dictionary:
            # print('hit {}'.format(firstword))
            return '{} {}'.format(firstword, max_match(remainder, dictionary))
    
    # no word was found, so make a one-character word
    firstword = sentence[0]
    remainder = sentence[1:]
    return '{} {}'.format(firstword, max_match(remainder, dictionary))


if __name__ == '__main__':
    dictionary = [
        '他',
        '特别',
        '喜欢',
        '北京烤鸭',
    ]

    sentence = '他特别喜欢北京烤鸭'
    
    print(max_match(sentence, dictionary))
        