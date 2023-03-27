# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class TestGildedRose:
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert len(items) == 1
        assert items[0].name == "foo"
        assert items[0].sell_in == -1
        assert items[0].quality == 0
