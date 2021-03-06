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
 
from Core.config import Config
from Core.maps import User
from Core.loadable import loadable, route

class whois(loadable):
    """Lookup a user's details"""
    usage = " <pnick>"
    
    @route(r"(\S+)", access = "member")
    def execute(self, message, user, params):

        # assign param variables 
        search=params.group(1)

        # do stuff here
        if search.lower() == Config.get("Connection","nick").lower():
            message.reply("I am %s. YOU ARE A GHEY!" % (Config.get("Connection","nick"),))
            return

        whore = User.load(name=search, exact=False, access="member") or User.load(name=search)
        if whore is None:
            message.reply("No users matching '%s'"%(search,))
            return

        reply=""
        if whore == user:
            reply+="You are %s, you are a %s" + (" and you are also known as %s" if whore.alias else "%s") + ". Your sponsor is %s. You have %s carebears."
        else:
            reply+="Information about %s; they are a %s" + (" and they are also known as %s" if whore.alias else "%s") + ". Their sponsor is %s. They have %s carebears."
        reply=reply%(whore.name,whore.level,whore.alias or "",whore.sponsor,whore.carebears,)

        message.reply(reply)
