from os.path \
    import join

path_to_downloads = '/tmp/downloads'

relative_path_to_downloaded_videos = 'videos'
relative_path_to_downloaded_dataset = 'dataset'


# Accessors
## Getters
def get_path_to_downloads() -> str:
    global path_to_downloads
    return path_to_downloads


def get_relative_path_to_downloaded_videos() -> str:
    global relative_path_to_downloaded_videos
    return relative_path_to_downloaded_videos


def get_relative_path_to_downloaded_dataset() -> str:
    global relative_path_to_downloaded_dataset
    return relative_path_to_downloaded_dataset


def get_full_path_to_downloaded_dataset() -> str:
    return join(
        get_path_to_downloads(), 
        get_relative_path_to_downloaded_dataset()
    )


def get_full_path_to_downloaded_videos() -> str:
    return join(
        get_path_to_downloads(), 
        get_relative_path_to_downloaded_videos()
    )


## Setters
def set_path_to_downloads(
        value: str
    ) -> None:
    global path_to_downloads
    path_to_downloads = value


def set_relative_path_to_downloaded_videos(
        value: str
    ) -> None:
    global relative_path_to_downloaded_videos
    relative_path_to_downloaded_videos = value


def set_relative_path_to_downloaded_dataset(
        value: str
    ) -> None:
    global relative_path_to_downloaded_dataset
    relative_path_to_downloaded_dataset = value
