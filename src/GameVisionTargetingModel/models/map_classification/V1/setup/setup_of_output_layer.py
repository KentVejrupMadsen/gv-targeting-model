from keras.layers \
    import \
    Flatten, \
    Dense

from src.GameVisionTargetingModel.variables.model_settings \
    import \
    get_number_of_labels, \
    get_last_layer_multiplier


def generate_output_layer(
    layers: list
):
    layers.append(
        Flatten()
    )

    layers.append(
        Dense(
            get_number_of_labels()
            *
            get_last_layer_multiplier()
        )
    )

    layers.append(
        Dense(
            get_number_of_labels()
        )
    )
