# -*- coding: utf-8 -*-


def doit(gameStat):
    pass


def getPosition(gameStat):
    i = gameStat.find("'in_action': ")
    i = i + 13
    return gameStat.substring(i, i + 1)