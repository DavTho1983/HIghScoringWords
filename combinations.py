class Combinations:

    def get_combinations(self, word):
        word_list = []

        for letter_index in range(len(word)):
            new_word_string = f"{word[letter_index]}_"
            for i in range(len(word)):
                if i != letter_index:
                    new_word_string += word[i]
            word_list.append(new_word_string)

        for word in word_list:
            temp_list = word.split('_')
            for remaining_letter_index in range(len(temp_list[1])):
                new_string = temp_list[0]
                new_string += temp_list[1][remaining_letter_index] + '_'
                for other_remaining_letter_index in range(len(temp_list[1])):
                    if other_remaining_letter_index != remaining_letter_index:
                        new_string += temp_list[1][other_remaining_letter_index]

                word_list.append(new_string)

        new_word_list = []
        for word in word_list:
            new_word_list.append(word.split('_')[0])

        return new_word_list