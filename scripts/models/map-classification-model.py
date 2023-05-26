from keras \
    import Sequential


from keras.layers \
    import \
        Rescaling, \
        Conv2D, \
        MaxPooling2D, \
        GlobalAveragePooling2D, \
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

    ml_layers.append(
        Conv2D(
            128, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        GlobalAveragePooling2D()
    )

    ml_layers.append(
        Conv2D(
            64, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            64, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            64, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            64, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )
    
    ml_layers.append(
        MaxPooling2D((2, 2))
    )


    ml_layers.append(
        Conv2D(
            32, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            32, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            32, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            32, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        MaxPooling2D((2, 2))
    )


    ml_layers.append(
        Conv2D(
            8, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            8, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            8, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        Conv2D(
            8, 
            get_channels(), 
            padding='same', 
            activation='relu'
        )
    )

    ml_layers.append(
        MaxPooling2D((2, 2))
    )


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



def generated_layers() -> list:
    global ml_layers

    if len(ml_layers) == 0:
        preprocessing_layers()
        neural_network_layers()
        classifier_layers()

    return ml_layers


def setup_classify_map_model():
    set_classify_map_model(
        Sequential(
            generated_layers()
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

