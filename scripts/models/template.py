channels = 3

vision_width = 128
vision_height = 128

categories = 4
last_layer_multiplier = 8


def get_last_layer_multiplier() -> int:
    global last_layer_multiplier
    return last_layer_multiplier


def set_last_layer_multiplier(
        value: int
    ) -> None:
    global last_layer_multiplier
    last_layer_multiplier = value


def get_categories() -> int:
    global categories
    return categories


def set_categories( 
        value: int 
    ) -> None:
    global categories
    categories = value


def get_channels() -> int:
    global channels
    return channels


def set_channels(
        value: int
    ) -> None:
    global channels
    channels = value


def get_vision_width() -> int:
    global vision_width
    return vision_width


def get_vision_height() -> int:
    global vision_width
    return vision_width


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
