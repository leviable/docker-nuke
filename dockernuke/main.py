import logging
import sys

import docker

logging.basicConfig(format='%(message)s', level=logging.INFO, stream=sys.stdout)


def main():
    client = docker.from_env()

    for running_container in client.containers.list():
        logging.info("Stopping container: {0}".format(running_container.name))
        running_container.stop()

    for container in client.containers.list(all=True):
        logging.info("Removing container: {0}".format(container.name))
        container.remove()

    for image in client.images.list():
        logging.info("Removing image: {0}".format(image.tags))
        client.images.remove(image.id)

    for volume in client.volumes.list():
        logging.info("Removing volume: {0}".format(volume.name))
        volume.remove()
