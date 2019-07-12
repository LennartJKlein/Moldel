from WikiWordDistribution.DataFilters.DataFilter import DataFilter

class Composite_Filter(DataFilter):
    def __init__(self):
        self.filters = []

    def add(self, filter):
        self.filters.append(filter)

    def filter(self, all_words, parsed_data, season):
        important_words = all_words
        for f in self.filters:
            important_words = f.filter(important_words, parsed_data, season)
        return important_words