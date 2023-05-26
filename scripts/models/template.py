# variables
channels = 3

vision_width = 128
vision_height = 128

number_of_categories = 0
categories = None

last_layer_multiplier = 8


# Accessors
## states
def is_categories_empty() -> bool:
    global categories
    return \
        (categories is None) or \
        (get_number_of_categories() == 0)


## getters
def get_categories() -> list|None:
    global categories
    return categories


def get_last_layer_multiplier() -> int:
    global last_layer_multiplier
    return last_layer_multiplier


def get_number_of_categories() -> int:
    global number_of_categories
    return number_of_categories


def get_channels() -> int:
    global channels
    return channels


def get_vision_width() -> int:
    global vision_width
    return vision_width


def get_vision_height() -> int:
    global vision_width
    return vision_width


## setters
def set_vision_width(
        value: int
    ) -> None:
    global vision_width
    vision_width = value


def set_vision_height(
        value: int
    ) -> None:
    global vision_width
    vision_width = value


def set_last_layer_multiplier(
        value: int
    ) -> None:
    global last_layer_multiplier
    last_layer_multiplier = value


def set_channels(
        value: int
    ) -> None:
    global channels
    channels = value


def set_number_of_categories( 
        value: int 
    ) -> None:
    global number_of_categories
    number_of_categories = value


def set_categories(
        value: list
    ) -> None:
    global categories

    if not (len(value) == get_number_of_categories()):
        set_number_of_categories(
            len(value)
        )

    categories = value
