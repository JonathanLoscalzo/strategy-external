from strategy import Strategy


class SomeStrategy(Strategy):
    def suggest(self):
        return "some-suggest"

    def train(self):
        return "some-train"

