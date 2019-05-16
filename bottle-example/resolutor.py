from typing import Type, Dict, Union

from strategy import Strategy, AnotherStrategy
from strategies.some_strategy import SomeStrategy

res: Dict[str, Type[Strategy]] = {
    "another": AnotherStrategy,
    "some": SomeStrategy
}


def strategy_resolutor(key, *params, **kwars):
    return res[key]()
