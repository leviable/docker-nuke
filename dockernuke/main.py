import click
import docker


def main(force=False):
    client = docker.from_env()

    for running_container in client.containers.list():
        click.echo("Stopping container: {0}".format(running_container.name))
        _docker_call(running_container.stop, force=force)

    for container in client.containers.list(all=True):
        click.echo("Removing container: {0}".format(container.name))
        _docker_call(container.remove, force=force)

    for image in client.images.list():
        click.echo("Removing image: {0}".format(image.tags))
        _docker_call(client.images.remove, image.id, force=force)

    for volume in client.volumes.list():
        click.echo("Removing volume: {0}".format(volume.name))
        _docker_call(volume.remove, force=force)


def _docker_call(method, *args, **kwargs):
    """ """
    try:
        method(*args, **kwargs)
    except docker.errors.APIError as exc:
        if exc.status_code != 409:
            raise
        msg = ("Stopping/removing failed with status code 409. "
               "Rerun with '--force' to force removal")
        click.echo(click.style(msg, fg='red'))
