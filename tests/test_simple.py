# -*- coding: utf-8 -*-
# Copyright (C) 2020 Famedly
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from twisted.trial import unittest
from . import get_invite_policies
from synapse.module_api.errors import Codes
from synapse.module_api import NOT_SPAM


class SimpleTestCase(unittest.TestCase):
    async def test_block_outgoing_invites(self):
        policies = get_invite_policies({"block_all_outgoing_invites": True})

        result = await policies.user_may_invite(
            "@alice:example.org", "@bob:localhost", "!room:example.org"
        )
        self.assertEqual(result, Codes.FORBIDDEN)

        result = await policies.user_may_invite(
            "@alice:example.org", "@bob:example.org", "!room:example.org"
        )
        self.assertEqual(result, Codes.FORBIDDEN)

        result = await policies.user_may_invite(
            "@alice:localhost", "@bob:example.org", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

        result = await policies.user_may_invite(
            "@alice:localhost", "@bob:localhost", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

    async def test_default_does_allow_invites(self):
        policies = get_invite_policies(config={})

        result = await policies.user_may_invite(
            "@alice:example.org", "@bob:localhost", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

        result = await policies.user_may_invite(
            "@alice:example.org", "@bob:example.org", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

        result = await policies.user_may_invite(
            "@alice:localhost", "@bob:example.org", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

        result = await policies.user_may_invite(
            "@alice:localhost", "@bob:localhost", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

    async def test_invite_block_can_be_disabled(self):
        policies = get_invite_policies({"block_all_outgoing_invites": False})

        result = await policies.user_may_invite(
            "@alice:example.org", "@bob:localhost", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

        result = await policies.user_may_invite(
            "@alice:example.org", "@bob:example.org", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

        result = await policies.user_may_invite(
            "@alice:localhost", "@bob:example.org", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)

        result = await policies.user_may_invite(
            "@alice:localhost", "@bob:localhost", "!room:example.org"
        )
        self.assertEqual(result, NOT_SPAM)
