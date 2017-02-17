#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
#  
#  Copyright 2017 notna <notna@apparat.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

__all__ = ["openDialog","saveDialog","pickFolder"]

import os

from . import version

try:
    from . import _nativefileselect
except ImportError:
    from . import fallback as _nativefileselect

def interpretResult(path):
    if (isinstance(path,str) or isinstance(path,bytes)) and len(path)!=0:
        return os.path.abspath(path)
    else:
        # To Prevent weird return values from the various implementations
        return None

def openDialog(filters=[],default=None):
    if default is None:
        return interpretResult(_nativefileselect.openDialog(filters))
    else:
        return interpretResult(_nativefileselect.openDialogWithDefault(filters,default))

def saveDialog(filters=[],default=None):
    if default is None:
        return interpretResult(_nativefileselect.saveDialog(filters))
    else:
        return interpretResult(_nativefileselect.saveDialogWithDefault(filters,default))

def pickFolder(default=None):
    raise NotImplementedError("Folder picking is currently not implemented")
