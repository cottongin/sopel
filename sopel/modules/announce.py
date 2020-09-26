# coding=utf-8
"""
announce.py - Sopel Announcement Plugin
Sends announcements to all channels the bot has joined.
Copyright © 2013, Elad Alfassa, <elad@fedoraproject.org>
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from sopel import plugin


def _chunks(items, size):
    """Break a list of items into groups.

    :param items: the collection of items to chunk
    :type items: :term:`iterable`
    :param int size: the size of each chunk
    """
    # from https://stackoverflow.com/a/312464/5991 with modified names for readability
    for delim in range(0, len(items), size):
        yield items[delim:delim + size]


@plugin.command('announce')
@plugin.example('.announce Some important message here')
@plugin.require_admin('Sorry, I can\'t let you do that', reply=True)
@plugin.output_prefix('[ANNOUNCEMENT] ')
def announce(bot, trigger):
    """Send an announcement to all channels the bot is in"""
    size = bot.isupport.get('TARGMAX', {}).get('PRIVMSG', 1)
    channels = _chunks(bot.channels.keys(), size)
    for cgroup in channels:
        bot.say(trigger.group(2), ','.join(cgroup))
    bot.reply('Announce complete.')
