#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  _nativefileselect.py
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

raise ImportError("Currently buggy")

import os
import inspect

import ctypes

try:
    _lib = ctypes.CDLL(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/libnativefiledialog.so.1.0.0",mode=ctypes.RTLD_GLOBAL)
except Exception:
    raise ImportError("Could not load c-library")

def _parseFilters(filters):
    return ";".join([f.lstrip("*.") for _,f in filters if f.lstrip("*.")!=""])

def openDialog(filters):
    print("*"*10)
    out = ctypes.create_string_buffer(128)
    print("*"*10)
    print(out.value,repr(out.value),ctypes.sizeof(out))
    print("...")
    o = _lib.NFD_OpenDialog(_parseFilters(filters),None,out)
    print("*"*10)
    _lib.NFD_GetError.restype = ctypes.c_char
    print(_lib.NFD_GetError())
    print(ctypes.get_errno())
    print("*"*10)
    c = ctypes.string_at(ctypes.addressof(out))
    print(c,len(c))
    print(ctypes.alignment(out))
    print(o)
    print(out.value,repr(out.value),ctypes.sizeof(out))
    return repr(out.value)
