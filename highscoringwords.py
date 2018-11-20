from combinations import Combinations


class HighScoringWords:
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """

        self.combinations = Combinations()
        self.leaderboard = []  # initialise an empty leaderboard
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self, new_list=None):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return:
        """

        if new_list == None:
            words_for_leaderboard = self.valid_words
        else:
            words_for_leaderboard = new_list

        word_scores = {}
        for word in words_for_leaderboard:
            score = 0
            for letter in word:
                score += self.letter_values[letter]
            word_scores[word] = score

        leaderboard = sorted([
            [(word, word_scores[word]) for word in sorted(word_scores, key=word_scores.get, reverse=True)]
        ])
        return leaderboard


    def build_leaderboard_for_letters(self, starting_letters, MAX_LEADERBOARD_LENGTH, MIN_WORD_LENGTH):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return:
        """
        c = Combinations()
        words_from_starting_letters = c.get_combinations(starting_letters)
        real_words = []

        for word in words_from_starting_letters:
            print(word)
            if word in self.valid_words:
                if len(word) >= MIN_WORD_LENGTH:
                    real_words.append(word)
        leaderboard = self.build_leaderboard_for_word_list(real_words)
        return leaderboard[:MAX_LEADERBOARD_LENGTH]

h = HighScoringWords()
print(h.build_leaderboard_for_letters("mace", 100, 3))