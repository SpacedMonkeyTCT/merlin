# This file is part of Merlin.
# Merlin is the Copyright (C)2008,2009,2010 of Robin K. Hansen, Elliot Rosemarine, Andreas Jacobsen.

# Individual portions may be copyright by individual contributors, and
# are included in this collective work with permission of the copyright
# owners.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
 
from Core.maps import Ship
from Core.loadable import loadable, route

class ship(loadable):
    """Returns the stats of the specified ship"""
    usage = " <ship>"
    
    @route(r"(\w+)")
    def execute(self, message, user, params):
        
        name = params.group(1)
        
        ship = Ship.load(name=name)
        if ship is None:
            message.alert("No Ship called: %s" % (name,))
            return
        message.reply(str(ship))
