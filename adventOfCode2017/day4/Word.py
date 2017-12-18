class Word:
    data: str
    charDict: dict

    def __init__(self, data):
        self.data = data

        self.charDict = self.__count_chars(data)

    def is_a_anagram_of(self, other: 'Word') -> bool:
        other_dict = self.__count_chars(other.data)
        return self.charDict == other_dict

    def __count_chars(self, string: str) -> dict:
        count_dict = dict()
        for character in string:
            if count_dict.get(character) is not None:
                count_dict[character] = count_dict[character] + 1
            else:
                count_dict[character] = 1
        return count_dict

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.data == o.data
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
