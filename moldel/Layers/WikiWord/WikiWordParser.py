from Data.Player import Player
from Data.WikiWord import Linker
from Data.WikiWord.Job import Job
from typing import Dict, Set, NamedTuple
import rootpath
import string

WikiWordData = NamedTuple("WikiWordData", [("job_frequency", Dict[Job, int]), ("number_words", int)])
class WikiWordParser:
    """ The Wiki Word Parser reads all wiki files of all players in the given seasons and converts it to interpretable
    and understandable features. """

    @staticmethod
    def parse(seasons: Set[int]) -> Dict[Player, WikiWordData]:
        """ Parse all the wiki files of all players that participated in these seasons to features.

        Parameters:
            seasons (Set[int]): The seasons for which we want to compute all features of the players that participated
            in these seasons.

        Returns:
            Dict[Player, WikiWordData]: A dictionary with as key the players and as value a Wiki Word Data tuple with
            as first value a dictionary with the frequency of all job for this player (so no job is excluded from the
            dictionary) and as second value the total number of words in the players wiki page.
        """
        data = dict()
        for player in Player:
            if player.value.season in seasons:
                data[player] = WikiWordParser.__feature_player_parse(player)
        return data

    @staticmethod
    def __feature_player_parse(player: Player) -> WikiWordData:
        """ Computes the features for a given player which are the frequencies of every Job and a total number of words
        in the players wiki page.

        Parameters:
            player (Player): The player for which we want to compute the features.

        Returns:
            WikiWordData: Which is a tuple with two values. The first value is a dictionary with Job as key and as value
            the total number of times each of the Job word occurs in the wiki page. The second value is the total number
            of words in the players wiki page.
        """
        file_path = rootpath.detect() + "/" + Linker.WIKI_FILES_PATH + Linker.LINKER[player]
        word_frequency = WikiWordParser.__wiki_file_parse(file_path)
        job_frequency = dict()
        for job in Job:
            job_frequency[job] = sum([word_frequency.get(word, 0) for word in job.value])

        number_words = sum(word_frequency.values())
        return WikiWordData(job_frequency, number_words)

    @staticmethod
    def __wiki_file_parse(file_path: str) -> Dict[str, int]:
        """ Will parse the word occurrences of a single wiki file.

        Parameters:
            file_path (str): The path to the file which will be parsed.

        Returns:
            Dict[str, int]: A dictionary with the frequency of words. The key is the word and the value is the frequency
            of that word. If a word is not included then it occurs 0 times.
        """
        file = open(file_path, "r", encoding="utf8")
        lines = file.readlines()
        word_occurrence = dict()
        for line in lines:
            filtered = WikiWordParser.__line_filter(line)
            split = filtered.split(" ")
            for word in split:
                pure_word = WikiWordParser.__word_filter(word)
                word_occurrence[pure_word] = word_occurrence.get(pure_word, 0) + 1
        return word_occurrence

    @staticmethod
    def __line_filter(line: str) -> str:
        """ Filter unwanted symbols/characters from a read line in the wiki file. """
        result = line.lower()
        for char in string.punctuation:  # Remove symbols from text
            result = result.replace(char, ' ')
        result = result.strip("\n")
        result = result.strip("\t")
        return result

    @staticmethod
    def __word_filter(word: str) -> str:
        """ Filter unwanted symbols/characters from a word in the wiki file.  """
        result = word.strip("\n")
        result = result.strip("\t")
        return result