# libraries
import random

# Variables
randomized_seed = 0
reset_seed:bool = False

# Accessors
## getters
def get_randomized_seed() -> int:
    global randomized_seed
    init_value()

    return randomized_seed

def get_is_to_reset_seed() -> bool:
    global reset_seed
    return reset_seed


## setters
def set_randomized_seed(
        value:int
    ) -> int:
    global randomized_seed
    randomized_seed = value
    return randomized_seed


def set_is_to_reset_seed(
        value:bool
) -> None:
    global reset_seed
    reset_seed = value


## states
def is_randomized_seed_zero() -> bool:
    global randomized_seed
    return randomized_seed == 0


## functions
def init_value() -> None:
    if is_randomized_seed_zero() or \
        get_is_to_reset_seed():
        system_random = random.SystemRandom()
        set_randomized_seed(
            system_random.randint(
                1,
                8388607
            )
        )
