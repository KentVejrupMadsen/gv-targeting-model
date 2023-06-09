from src.GameVisionTargetingModel.models.classification.map \
    import MapClassifierVersion1


def test_make() -> None:
    classifier = MapClassifierVersion1()
    classifier.summary()

