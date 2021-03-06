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

class TestHelloWorldBot(BotTestCase):
    bot_name = "helloworld"

    def test_bot(self):
        self.assert_bot_output(
            {'content': "foo", 'type': "private", 'sender_email': "foo"},
            "beep boop"
        )
        self.assert_bot_output(
            {'content': "Hi, my name is abc", 'type': "stream", 'display_recipient': "foo", 'subject': "foo"},
            "beep boop"
        )
        self.assert_bot_output(
            {'content': "", 'type': "stream", 'display_recipient': "foo", 'subject': "foo"},
            "beep boop"
        )
