import logging
import sys

import docker

logging.basicConfig(format='%(message)s', level=logging.INFO, stream=sys.stdout)


def main(force=False):
    client = docker.from_env()

    for running_container in client.containers.list():
        logging.info("Stopping container: %s", running_container.name)
        running_container.stop(force=force)

    for container in client.containers.list(all=True):
        logging.info("Removing container: %s", container.name)
        container.remove(force=force)

    for image in client.images.list():
        logging.info("Removing image: %s", image.tags)
        client.images.remove(image.id, force=force)

    for volume in client.volumes.list():
        logging.info("Removing volume: %s", volume.name)
        volume.remove(force=force)
