from keras.models \
    import Sequential

from src.GameVisionTargetingModel.models.classification.map.v1.layers \
    import generate_layers_for_map_classifier_v1


class MapClassifier(
    Sequential
):
    def __init__(self):
        super().__init__(
            generate_layers_for_map_classifier_v1()
        )

        self.compile()
