# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## SNMP utilities
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import re


rx_os_format = re.compile(r"(?P<repeat>[*]?)(?P<size>\d+)(?P<format>[xdoat])(?P<dsep>[^*0-9]?)(?P<rt>[^*0-9]?)")

def render_tc(value, base_type, format=None):
    """
    Render SNMP TC using DISPLAY-HINT according to RFC 2579
    
    :param value: Binary string
    :param base_type: Basic SNMP TC Type
    :param format: Optional format string (DISPLAY-HINT)
    
    Integer32 formatting
    >>> render_tc(1234, "Integer32")
    '1234'
    >>> render_tc(1234, "Integer32", "x")
    '4d2'
    >>> render_tc(1234, "Integer32", "o")
    '2322'
    >>> render_tc(1234, "Integer32", "d")
    '1234'
    >>> render_tc(1234, "Integer32", "d-2")
    '12.34'
    >>> render_tc(1234, "Integer32", "d-4")
    '0.1234'
    >>> render_tc(1234, "Integer32", "d-6")
    '0.001234'
    
    OctetString formatting
    >>> render_tc("\x80", "OctetString", "1x")
    '80'
    >>> render_tc("\x80\xff", "OctetString", "2x")
    '80ff'
    >>> render_tc("\x01\x02\x03\x04", "OctetString", "1d:1d:1d:1d")
    '1:2:3:4'
    >>> render_tc("\x80", "OctetString", "1d")
    '128'
    >>> render_tc("\x80\xff", "OctetString", "2d")
    '33023'
    >>> render_tc("\x80", "OctetString", "1o")
    '200'
    >>> render_tc("\x04\x74\x65\x73\x74", "OctetString", "*1a")
    'test'
    >>> render_tc("\x74\x65\x73\x74", "OctetString", "255a")
    'test'
    """
    if base_type == "Integer32":
        if format == "x":
            # Hexadecimal
            return "%x" % value
        elif format == "o":
            # Octal
            return "%o" % value
        elif format == "b":
            # Binart
            pass
        elif format == "d":
            return str(value)
        elif format and format.startswith("d"):
            if format[1] == "-":
                p = int(format[2:])
                v = str(value)
                if len(v) <= p:
                    v = "0" * (p - len(v) + 1) + v
                return "%s.%s" % (v[:-p], v[-p:])
    elif base_type == "OctetString":
        value = [ord(c) for c in value]
        r = ""
        for match in rx_os_format.finditer(format):
            repeat, size, format, dsep, rt = match.groups()
            size = int(size)
            if repeat:
                repeat = value.pop(0)
            else:
                repeat = 1
            rr = []
            for i in range(repeat):
                v = 0
                for j in range(size):
                    v = (v << 8) + value.pop(0)
                if format == "x":
                    rr += ["%x" % v]
                elif format == "d":
                    rr += ["%d" % v]
                elif format == "o":
                    rr += ["%o" % v]
                elif format == "a":
                    rr += [chr(v)]
                else:
                    # @todo: "t" format
                    raise ValueError("Unknown format: %s" % format)
            # Join with repeat separator
            r += rt.join(rr)
            #
            r += dsep
        return r
    return str(value)
