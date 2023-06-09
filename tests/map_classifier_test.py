from src.GameVisionTargetingModel.models.classification\
    import MapClassifierVersion1


def test_make() -> None:
    classifier = MapClassifierVersion1()
    classifier.summary()

