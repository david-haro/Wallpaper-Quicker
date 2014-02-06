#!/usr/bin/env python
#
# Copyright 2009 Canonical Ltd.
#
# Authors: Neil Jagdish Patel <neil.patel@canonical.com>
#          Jono Bacon <jono@ubuntu.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of either or both of the following licenses:
#
# 1) the GNU Lesser General Public License version 3, as published by the
# Free Software Foundation; and/or
# 2) the GNU Lesser General Public License version 2.1, as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the applicable version of the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of both the GNU Lesser General Public
# License version 3 and version 2.1 along with this program.  If not, see
# <http://www.gnu.org/licenses>
#
 
import gobject, gtk, appindicator, os, os.path
 
def menuitem_response(w, buf):
    if os.path.isfile("BlueCloud.jpg"):
      bashJoined = 'gsettings set org.gnome.desktop.background picture-uri file:///home/deedoo/Pictures/Wall/'+ buf
      os.system(bashJoined) 


if __name__ == "__main__":
  ind = appindicator.Indicator ("example-simple-client",
                              "playlist-automatic-symbolic",
                              appindicator.CATEGORY_APPLICATION_STATUS)
  ind.set_status (appindicator.STATUS_ACTIVE)
  ind.set_attention_icon ("indicator-messages-new")
 
  menu = gtk.Menu()
 

  for i in range(len([name for name in os.listdir('.') if os.path.isfile(name)])): #lists file names in dir
    buf = os.listdir(".")[i] #gives number of files in dir
 
    if "jpg" in buf or "png" in buf:

      menu_items = gtk.MenuItem(buf)
 
      menu.append(menu_items)
 
    # this is where you would connect your menu item up with a function:
 
      menu_items.connect("activate", menuitem_response, buf)
 
    # show the items
      menu_items.show()
  
  menu_items = gtk.MenuItem("Quit!")
  menu.append(menu_items)
  menu_items.connect("activate", gtk.main_quit)
  menu_items.show()

  ind.set_menu(menu)
 
  gtk.main()
