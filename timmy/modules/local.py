#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from timmy.nodes import NodeManager as BaseNodeManager


def add_args(parser):
    parser.add_argument('-j', '--nodes-json', required=True,
                        help=('Path to a json file containing host info:'
                              ' ip, roles, etc.'))
    return parser


def check_args(args, conf):
    pass


def add_conf(conf):
    pass


class NodeManager(BaseNodeManager):
    pass
