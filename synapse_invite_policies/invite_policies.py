# -*- coding: utf-8 -*-
# Copyright (C) 2020,2023 Famedly
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
from typing import Union, Literal
import logging

from synapse.module_api import ModuleApi, NOT_SPAM, errors

logger = logging.getLogger(__name__)


class InvitePoliciesConfig:
    block_all_outgoing_invites = False


class InvitePolicies:
    __version__ = "0.0.0"

    def __init__(self, config: InvitePoliciesConfig, api: ModuleApi):
        self.api = api

        self.config = config
        if self.config.block_all_outgoing_invites:
            self.api.register_spam_checker_callbacks(
                user_may_invite=self.user_may_invite
            )

    # pylint: disable=unused-argument
    async def user_may_invite(
        self, inviter: str, invitee: str, room_id: str
    ) -> Union[Literal["NOT_SPAM"], errors.Codes]:
        if self.config.block_all_outgoing_invites and self.api.is_mine(inviter):
            print(f"is mine {inviter}")
            return errors.Codes.FORBIDDEN
        return NOT_SPAM

    @staticmethod
    def parse_config(config):
        _config = InvitePoliciesConfig()
        _config.block_all_outgoing_invites = config.get(
            "block_all_outgoing_invites", False
        )
        return _config
