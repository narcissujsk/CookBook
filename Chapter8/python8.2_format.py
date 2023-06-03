_format = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _format[format_spec]
        return fmt.format(d=self)


if __name__ == "__main__":
    d = Date(2222, 22, 22)
    print(format(d, 'mdy'))
    print(format(d))
    print(format(d, 'dmy'))
    print('{:dmy}'.format(d))

