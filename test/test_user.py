"""
Test user, a simple data container for a user.
"""

import sys
sys.path.append('.')

import py.test

from tiddlyweb.user import User

usersign = 'cdent'
note = 'for future expansion'

def setup_module(module):
    pass

def test_user_create():
    user = User('cdent')
    assert type(user) == User

    assert user.usersign == 'cdent'
    user.note = note
    assert user.note == note

    user.note = 'bar'
    assert user.note == 'bar'

def test_user_args():
    py.test.raises(TypeError, 'user = User()')

def test_user_stringification():
    user = User('monkey')

    assert 'monkey' in '%s' % user

def test_user_password():
    user = User('monkey')
    user.set_password('cowpig')

    assert user.check_password('cowpig'), 'correct password returns true'
    assert not user.check_password('pigcow'), 'bad password returns false'
