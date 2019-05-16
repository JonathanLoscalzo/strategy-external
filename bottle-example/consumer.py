from resolutor import strategy_resolutor


def consume_train(strategy, *params, **kwargs):
    return strategy_resolutor(strategy).train()


def consume_suggest(strategy, *params, **kwargs):
    strategy_resolutor(strategy).suggest()

