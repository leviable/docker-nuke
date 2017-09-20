import docker


def main():
    client = docker.from_env()

    for running_container in client.containers.list():
        print("Stopping container: {0}".format(running_container.name))
        running_container.stop()

    for container in client.containers.list(all=True):
        print("Removing container: {0}".format(container.name))
        container.remove()

    for image in client.images.list():
        print("Removing image: {0}".format(image.tags))
        client.images.remove(image.id)

    for volume in client.volumes.list():
        print("Removing volume: {0}".format(volume.name))
        volume.remove()
