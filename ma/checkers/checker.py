# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 IBM Corporation

Licensed under the Apache License, Version 2.0 (the “License”);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an “AS IS” BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

    Contributors:
        * Diego Fernandez-Merjildo <merjildo@br.ibm.com>
        * Rafael Peria de Sene <rpsene@br.ibm.com>
"""

import abc


class Checker(object):
    """ Abstract class Checker """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def check(self, node):
        """ Check node from AST"""
        raise NotImplementedError('users must define __check__ to use this base class')

    @abc.abstractmethod
    def get_pattern_hint(self):
        """Return the pattern that should be used to get the problematics files"""
        raise NotImplementedError('users must define __get_pattern_hint__ to use this base class')

    @abc.abstractmethod
    def get_description(self):
        """Return the description of the checker"""
        raise NotImplementedError('users must define __get_description__ to use this base class')
