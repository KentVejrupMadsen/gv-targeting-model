from keras.layers \
    import \
    Rescaling

from src.GameVisionTargetingModel.variables \
    import \
    get_input_set


def generate_input_layer(
    layers: list
):
    layers.append(
        Rescaling(
            1./255,
            input_shape=get_input_set()
        )
    )

