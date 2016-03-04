#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest
from unittest.mock import MagicMock

from gns3.controller import Controller
from gns3.server import Server


@pytest.fixture
def controller():
    return Controller(MagicMock())


def test_http_query_forwarded_to_http_client(controller):
    """
    The HTTP query should be forwarded to the HTTP client
    """
    controller.get("/get")
    controller._http_client.get.assert_called_with("/get")
    controller.post("/post")
    controller._http_client.post.assert_called_with("/post")
    controller.put("/put")
    controller._http_client.put.assert_called_with("/put")
    controller.delete("/delete")
    controller._http_client.delete.assert_called_with("/delete")


def test_add_server(controller):

    server = Server({"server_id": "local", "host": "example.com", "port": 42}, MagicMock())
    controller.addServer(server)
    controller._http_client.post.assert_called_with("/servers", None, body={'host': 'example.com', 'port': 42, 'password': None, 'server_id': 'local', 'protocol': 'http', 'user': None})
