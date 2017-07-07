#!/usr/bin/python3
# -*- coding: utf-8 -*-

import adbs
import os
import signal
from datetime import date

try:
    import gi
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as ai
    from gi.repository import Gtk as gtk
    from gi.repository import GObject as gobject
except ImportError:
    print('Repository version required is not available!!')
    exit(1)

APPINDICATOR_ID = 'nepcal-applet'
indicator = ai.Indicator.new(APPINDICATOR_ID,
                             os.path.abspath('nepaliflag.png'),
                             ai.IndicatorCategory.OTHER)


def get_today():
    os.environ['TZ'] = 'Asia/Kathmandu'
    today = date.today().strftime('%Y/%m/%d')
    bs_today = adbs.ad_to_bs(today)['ne']
    return '{} {} {}, {}'.format(bs_today['year'], bs_today['str_month'],
                                 bs_today['day'], bs_today['str_day_of_week'])


def set_label():
    indicator.set_label(get_today(), "")
    return True


def menu():
    menu = gtk.Menu()
    item_convert = gtk.MenuItem('Date Converter')
    item_convert.connect('activate', open_convert_dialog)
    menu.append(item_convert)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu


def open_convert_dialog(src):
    dialog = gtk.Dialog('Convert AD to BS and Vice Versa',
                        None, 1)
    dialog.set_default_size(250, 250)
    dialog.show_all()


def quit(src):
    gtk.main_quit()


def main():
    indicator.set_status(ai.IndicatorStatus.ACTIVE)
    set_label()
    gobject.timeout_add(5000, set_label)
    indicator.set_menu(menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()


if __name__ == '__main__':
    main()
