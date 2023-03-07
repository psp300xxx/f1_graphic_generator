import math


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

def __millis_representation__(millis: float)-> str:
    millis_str = str(int(millis))
    assert len(millis_str) <= 3
    if len(millis_str) == 3:
        return "{}".format(millis_str)
    elif len(millis_str) == 2:
        return "0{}".format(millis_str)
    return "00{}".format(millis_str)


def float_to_time( time : float ) -> str:
    minutes = int((time/1000)//60)
    assert len(str(minutes)) == 1
    seconds = ((time/1000)/60 - minutes) * 60
    if close_enough(seconds, float(int(seconds)+1) ):
        seconds = int(seconds)+1
    seconds = int(seconds)
    assert len(str(seconds))<=2
    millis = time - ( minutes *1000*60  ) - (seconds * 1000)
    if minutes == 0:
        return "{}.{}".format(seconds, __millis_representation__(millis))
    if millis == 0:
        return "{}:{}".format(int(minutes), seconds)
    return "{}:{}.{}".format(int(minutes), seconds, __millis_representation__(millis))

def close_enough(a: float, b: float, eps: float= 1E-6) -> bool:
    diff = a-b
    return abs(diff)<eps