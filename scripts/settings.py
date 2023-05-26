split_dataset_at = 0.35
update_frequency = 1


def get_split_dataset_at() -> float:
    global split_dataset_at
    return split_dataset_at


def get_update_frequency() -> int:
    global update_frequency
    return update_frequency


def set_update_frequency(value: int) -> None:
    global update_frequency
    update_frequency = value


def set_split_dataset_at(value) -> None:
    global split_dataset_at
    split_dataset_at = value
