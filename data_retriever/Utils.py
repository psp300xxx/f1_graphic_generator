def time_to_float( time : str ) -> float:
    min_to_sec_divider = ":"
    sec_to_millis_divider = "."
    splits = time.split(min_to_sec_divider)
    has_minutes = len(splits) == 2
    if has_minutes:
        minutes = splits[0]
    else:
        minutes = 0
    index = 1 if has_minutes else 0
    splits = splits[index].split(sec_to_millis_divider)
    has_millis = len(splits) == 2
    seconds = splits[0]
    if has_millis:
        millis = splits[1]
    else:
        millis = 0
    return float(millis) + float(seconds)*1000 + float(minutes)*1000*60