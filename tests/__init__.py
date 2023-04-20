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

from mock import Mock
from synapse_invite_policies import InvitePolicies

from synapse.server import HomeServer
from synapse.module_api import ModuleApi

admins = {}


def get_invite_policies(config: dict):
    def is_mine(user_id: str):
        return user_id.endswith(":example.org")

    hs = Mock(HomeServer, hostname="example.org")

    api = Mock(ModuleApi)
    api._hs = hs
    api.server_name = "example.org"
    api.is_mine.side_effect = is_mine

    return InvitePolicies(InvitePolicies.parse_config(config), api)
