import logging


def create_uri(settings):
    logging.debug("Creating uri")

    if settings["driver"].strip().lower() == "sqlite":
        uri = f"sqlite://{settings['file']}"
    else:
        uri = (
            f"{settings['driver']}://"
            f"{settings['username']}:{settings['password']}"
            f"@{settings['host']}/{settings['database']}"
        )

    return uri
