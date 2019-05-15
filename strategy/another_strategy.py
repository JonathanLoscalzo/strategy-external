from strategy import Strategy


class AnotherStrategy(Strategy):
    def suggest(self):
        return "Another - suggest"

    def train(self):
        return "Another - train"
