#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function

import os
import sys

our_dir = os.path.dirname(os.path.abspath(__file__))
# For dev setups, we can find the API in the repo itself.
if os.path.exists(os.path.join(our_dir, '..')):
    sys.path.insert(0, '..')
from bots_test_lib import BotTestCase

class TestVirtualFsBot(BotTestCase):
    bot_name = "virtual_fs"

    def test_bot(self):
        self.assert_bot_output(
            {'content': "cd /home", 'type': "private", 'display_recipient': "foo", 'sender_email': "foo_sender@zulip.com"},
            "foo_sender@zulip.com:\nERROR: invalid path"
        )
        self.assert_bot_output(
            {'content': "mkdir home", 'type': "stream", 'display_recipient': "foo", 'subject': "foo", 'sender_email': "foo_sender@zulip.com"},
            "foo_sender@zulip.com:\ndirectory created"
        )
        self.assert_bot_output(
            {'content': "pwd", 'type': "stream", 'display_recipient': "foo", 'subject': "foo", 'sender_email': "foo_sender@zulip.com"},
            "foo_sender@zulip.com:\n/"
        )
        self.assert_bot_output(
            {'content': "help", 'type': "stream", 'display_recipient': "foo", 'subject': "foo", 'sender_email': "foo_sender@zulip.com"},
            ('foo_sender@zulip.com:\n\nThe "fs" commands implement a virtual file system for a stream.\n'
             'The locations of text are persisted for the lifetime of the bot\n'
             'running, and if you rename a stream, you will lose the info.\n'
             'Example commands:\n\n```\n'
             'fs sample_conversation: sample conversation with the bot\n'
             'fs mkdir: create a directory\n'
             'fs ls: list a directory\n'
             'fs cd: change directory\n'
             'fs pwd: show current path\n'
             'fs write: write text\n'
             'fs read: read text\n'
             'fs rm: remove a file\n'
             'fs rmdir: remove a directory\n'
             '```\n'
             'Use commands like `fs help write` for more details on specific\ncommands.\n'),
        )
        self.assert_bot_output(
            {'content': "help ls", 'type': "stream", 'display_recipient': "foo", 'subject': "foo", 'sender_email': "foo_sender@zulip.com"},
            "foo_sender@zulip.com:\nsyntax: ls <optional_path>"
        )
        self.assert_bot_output(
            {'content': "", 'type': "stream", 'display_recipient': "foo", 'subject': "foo", 'sender_email': "foo_sender@zulip.com"},
            ('foo_sender@zulip.com:\n\nThe "fs" commands implement a virtual file system for a stream.\n'
             'The locations of text are persisted for the lifetime of the bot\n'
             'running, and if you rename a stream, you will lose the info.\n'
             'Example commands:\n\n```\n'
             'fs sample_conversation: sample conversation with the bot\n'
             'fs mkdir: create a directory\n'
             'fs ls: list a directory\n'
             'fs cd: change directory\n'
             'fs pwd: show current path\n'
             'fs write: write text\n'
             'fs read: read text\n'
             'fs rm: remove a file\n'
             'fs rmdir: remove a directory\n'
             '```\n'
             'Use commands like `fs help write` for more details on specific\ncommands.\n'),
        )
