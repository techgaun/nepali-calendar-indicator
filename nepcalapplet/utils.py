# -*- coding: utf-8 -*-


def format_output_date(date, lang='ne'):
    if lang:
        date = date[lang]
    return '{} {} {}, {}'.format(date['year'], date['str_month'], date['day'],
                                 date['str_day_of_week'])


def format_input_date(year, month, day):
    return '{}/{}/{}'.format(year, month, day)
