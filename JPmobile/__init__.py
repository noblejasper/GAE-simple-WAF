# -*- coding: utf-8 -*-
import re

DOCOMO_RE   = re.compile(r'^DoCoMo/\d\.\d[ /]')
SOFTBANK_RE = re.compile(r'^(?:(?:SoftBank|Vodafone|J-PHONE)/\d\.\d|MOT-)')
EZWEB_RE    = re.compile(r'^(?:KDDI-[A-Z]+\d+[A-Z]? )?UP\.Browser\/')
WILLCOM_RE  = re.compile(r'^Mozilla/3\.0\((?:DDIPOCKET|WILLCOM);|^Mozilla/4\.0 \(compatible; MSIE (?:6\.0|4\.01); Windows CE; SHARP/WS\d+SH; PPC; \d+x\d+\)')

def detect_fast(useragent):
    """
    return name of Japanese mobile carriers from a given useragent string.
    if the agent isn't mobile one, then returns 'nonmobile'.
    """
    if DOCOMO_RE.match(useragent):
        return "docomo"
    elif EZWEB_RE.match(useragent):
        return "ezweb"
    elif SOFTBANK_RE.match(useragent):
        return "softbank"
    elif WILLCOM_RE.match(useragent):
        return "willcom"
    else:
        return "nonmobile"

def is_mobile(useragent):
    carrier = detect_fast(useragent)
    if carrier == "docomo" or carrier == "ezweb" or carrier == "softbank":
        return True
    else:
        return None
