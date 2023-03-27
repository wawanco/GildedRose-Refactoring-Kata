# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class TestGildedRose:
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert "foo" == items[0].name
