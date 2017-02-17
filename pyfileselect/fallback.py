#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fallback.py
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

import sys
import os

def _parseFilters(filters):
    return filters

if sys.version_info.major==2:
    from Tkinter import Tk
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    
    def openDialog(filters,default=None):
        from tkFileDialog import askopenfilename
        return askopenfilename(filetypes=_parseFilters(filters),initialdir=default)
    openDialogWithDefault=openDialog
    
    def saveDialog(filters,default=None):
        from tkFileDialog import asksaveasfilename
        return asksaveasfilename(filetypes=_parseFilters(filters),initialdir=default)
    saveDialogWithDefault=saveDialog
else:
    from tkinter import Tk
    Tk().withdraw()
    
    def openDialog(filters,default=None):
        from tkinter.filedialog import askopenfilename
        return askopenfilename(filetypes=_parseFilters(filters),initialdir=default)
    openDialogWithDefault=openDialog
    
    def saveDialog(filters,default=None):
        from tkinter.filedialog import asksaveasfilename
        return asksaveasfilename(filetypes=_parseFilters(filters),initialdir=default)
    saveDialogWithDefault=saveDialog
