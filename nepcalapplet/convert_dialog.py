# -*- coding: utf-8 -*-

import adbs
from .utils import format_output_date, format_input_date
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk as gtk
except ImportError:
    print('GTK Version 3 not available')
    exit(1)


class ConverterDialog(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.choice = 'ad2bs'
        self.set_title('Convert AD to BS and Vice Versa')
        self.set_default_size(350, 200)

        dialog_box = gtk.Box(spacing=6, orientation=gtk.Orientation.VERTICAL)
        self.add(dialog_box)

        ad2bs_btn = gtk.RadioButton.new_with_label_from_widget(None, 'AD to BS')
        ad2bs_btn.connect('toggled', self.handle_convert_choice, 'ad2bs')
        dialog_box.pack_start(ad2bs_btn, False, False, 0)

        bs2ad_btn = gtk.RadioButton.new_from_widget(ad2bs_btn)
        bs2ad_btn.set_label('BS to AD')
        bs2ad_btn.connect('toggled', self.handle_convert_choice, 'bs2ad')
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

        self.year_text = gtk.Entry(max_length=4, width_chars=6)
        grid.attach(self.year_text, 0, 2, 1, 2)
        self.month_text = gtk.Entry(max_length=2, width_chars=2)
        grid.attach(self.month_text, 1, 2, 1, 2)
        self.day_text = gtk.Entry(max_length=2, width_chars=2)
        grid.attach(self.day_text, 2, 2, 1, 2)

        convert_btn = gtk.Button.new_with_label('Convert')
        convert_btn.connect('clicked', self.handle_convert)
        grid.attach(convert_btn, 0, 4, 1, 2)

        self.convert_label = gtk.Label('')
        grid.attach(self.convert_label, 1, 6, 1, 3)

    def handle_convert_choice(self, _rbtn, choice):
        self.choice = choice

    def handle_convert(self, _btn):
        result = None
        if self.choice == 'ad2bs':
            ad_year = self.year_text.get_text()
            ad_month = self.month_text.get_text()
            ad_day = self.day_text.get_text()
            date = format_input_date(ad_year, ad_month, ad_day)
            result = format_output_date(adbs.ad_to_bs(date))
        elif self.choice == 'bs2ad':
            bs_year = self.year_text.get_text()
            bs_month = self.month_text.get_text()
            bs_day = self.day_text.get_text()
            date = format_input_date(bs_year, bs_month, bs_day)
            result = format_output_date(adbs.bs_to_ad(date), None)

        self.convert_label.set_text(result)
