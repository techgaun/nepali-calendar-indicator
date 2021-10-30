# -*- coding: utf-8 -*-

import adbs
import signal
from datetime import date
from os import path, environ
from .convert_dialog import ConverterDialog
from .utils import format_output_date


basedir = path.abspath(path.dirname(__file__))
icon_file = path.join(basedir, 'assets', 'nepaliflag.png')

try:
    import gi
    gi.require_version('AppIndicator3', '0.1')
    gi.require_version('Gtk', '3.0')
    from gi.repository import AppIndicator3 as ai
    from gi.repository import Gtk as gtk
    from gi.repository import GObject as gobject
except ImportError:
    print('Repository version required is not available!!')
    exit(1)

APPINDICATOR_ID = 'nepcal-applet'
indicator = ai.Indicator.new(APPINDICATOR_ID,
                             icon_file,
                             ai.IndicatorCategory.OTHER)


def get_today():
    environ['TZ'] = 'Asia/Kathmandu'
    today = date.today().strftime('%Y/%m/%d')
    bs_today = adbs.ad_to_bs(today)
    return format_output_date(bs_today)


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


def open_convert_dialog(_src):
    window = ConverterDialog()
    window.show_all()


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
