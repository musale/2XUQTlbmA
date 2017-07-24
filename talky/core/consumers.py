"""Handle basic connection between client and server."""
from channels import Group


def ws_connect(message):
    """Add a connected user to the 'users' group."""
    Group('users').add(message.reply_channel)


def ws_disconnect(message):
    """Remove a disconnected user from the 'user' group."""
    Group('users').discard(message.reply_channel)
