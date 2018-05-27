import click
import docker


def main(force=False):
    """ Finds and stops/removes all docker containers, images, and volumes """
    client = docker.from_env()

    for running_container in client.containers.list():
        echo_msg = "Stopping container {0}: ".format(running_container.short_id)
        _docker_call(running_container.stop, echo_msg, timeout=2)

    for container in client.containers.list(all=True):
        echo_msg = "Removing container {0}: ".format(container.short_id)
        _docker_call(container.remove, echo_msg, force=force)

    for image in client.images.list():
        echo_msg = "Removing image     {0}: ".format(image.short_id.split(':')[-1])
        _docker_call(client.images.remove, echo_msg, image.id, force=force)

    for volume in client.volumes.list():
        echo_msg = "Removing volume    {0}: ".format(volume.short_id)
        _docker_call(volume.remove, echo_msg, force=force)


def _docker_call(method, msg, *args, **kwargs):
    """ Calls `method`, echoing `msg`, and passing `*args` and `**kwargs` to the method """
    click.echo(msg, nl=False)
    try:
        method(*args, **kwargs)
    except docker.errors.APIError as exc:
        if exc.status_code != 409:
            raise
        click.secho('Failed (retry with "--force")', fg='red')
    else:
        click.secho('Succeeded', fg='green')
