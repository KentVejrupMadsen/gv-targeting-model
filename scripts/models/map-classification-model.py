from keras \
    import Sequential

from keras.layers \
    import \
        Rescaling, \
        Conv2D, \
        MaxPool2D, \
        Flatten, \
        Dense

from scripts.models.template \
    import \
        get_channels, \
        get_vision_height, \
        get_vision_width, \
        get_categories, \
        get_last_layer_multiplier


ml_map_model = None
ml_layers = []


def preprocessing_layers() -> None:
    global ml_layers

    ml_layers.append(
        Rescaling(
            1./255, 
            input_shape=(
                get_vision_height(), 
                get_vision_width(), 
                get_channels()
            )
        )
    )


def neural_network_layers() -> None:
    global ml_layers



def classifier_layers() -> None:
    global ml_layers
    ml_layers.append(
        Flatten()
    )

    ml_layers.append(
        Dense(
            get_last_layer_multiplier() * get_categories(), 
            activation='relu'
        )
    )

    ml_layers.append(
        Dense(
            get_categories()
        )
    )



def generate_layers() -> list:
    global ml_layers

    preprocessing_layers()
    neural_network_layers()
    classifier_layers()

    return ml_layers


def setup_classify_map_model():
    set_classify_map_model(
        Sequential(
            generate_layers()
        )
    )


def get_classify_map_model():
    global ml_map_model

    if ml_map_model is None:
        setup_classify_map_model()

    return ml_map_model


def set_classify_map_model( 
        value: Sequential 
    ):
    global ml_map_model
    ml_map_model = value

