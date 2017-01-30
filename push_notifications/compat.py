from __future__ import unicode_literals


def _user_is_authenticated(user):
    """Supports both the user.is_authenticated (post-1.10)
    and user.is_authenticated() (pre-2.0) API in Django.

    This can be retired once Django 1.10 is the minimum supported
    Django version.
    """
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated
