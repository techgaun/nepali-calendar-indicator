#!/usr/bin/python3
# -*- coding: utf-8 -*-

import adbs
import os
import signal
from datetime import date

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
                             os.path.abspath('nepaliflag.png'),
                             ai.IndicatorCategory.OTHER)

CONVERSION_CHOICE = 'ad2bs'
CONVERSION_LABEL = gtk.Label('')


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


def handle_convert_choice(widget, data=None):
    global CONVERSION_CHOICE
    CONVERSION_CHOICE = data


def handle_convert(btn):
    print(btn)


def open_convert_dialog(_src):
    window = gtk.Window()
    window.set_title('Convert AD to BS and Vice Versa')
    window.set_default_size(350, 200)

    dialog_box = gtk.Box(spacing=6, orientation=gtk.Orientation.VERTICAL)
    window.add(dialog_box)

    ad2bs_btn = gtk.RadioButton.new_with_label_from_widget(None, 'AD to BS')
    ad2bs_btn.connect('toggled', handle_convert_choice, 'ad2bs')
    dialog_box.pack_start(ad2bs_btn, False, False, 0)

    bs2ad_btn = gtk.RadioButton.new_from_widget(ad2bs_btn)
    bs2ad_btn.set_label('BS to AD')
    bs2ad_btn.connect('toggled', handle_convert_choice, 'bs2ad')
    dialog_box.pack_start(bs2ad_btn, False, False, 0)

    separator = gtk.HSeparator()
    dialog_box.pack_start(separator, False, True, 0)

    grid = gtk.Grid()
    grid.set_column_spacing(100)
    dialog_box.pack_start(grid, False, False, 0)

    year_label = gtk.Label('Year')
    grid.attach(year_label, 0, 1, 1, 1)
    month_label = gtk.Label('Month')
    grid.attach(month_label, 1, 1, 1, 1)
    day_label = gtk.Label('Day')
    grid.attach(day_label, 2, 1, 1, 1)

    year_text = gtk.Entry(max_length=4, width_chars=6)
    grid.attach(year_text, 0, 2, 1, 2)
    month_text = gtk.Entry(max_length=2, width_chars=2)
    grid.attach(month_text, 1, 2, 1, 2)
    day_text = gtk.Entry(max_length=2, width_chars=2)
    grid.attach(day_text, 2, 2, 1, 2)

    convert_btn = gtk.Button.new_with_label('Convert')
    convert_btn.connect('clicked', handle_convert)
    grid.attach(convert_btn, 0, 4, 1, 2)

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
