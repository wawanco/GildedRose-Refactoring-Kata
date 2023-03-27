# -*- coding: utf-8 -*-
import unittest
from typing import List

import pytest

from gilded_rose import Item, GildedRose


def do_update_one(
        name,
        initial_sell_in,
        initial_quality,
        final_sell_in,
        final_quality
):
    items = [Item(name, initial_sell_in, initial_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert len(items) == 1
    assert items[0].name == name
    assert items[0].sell_in == final_sell_in
    assert items[0].quality == final_quality


class TestGildedRoseFoo:
    @pytest.mark.parametrize(
        "name, initial_sell_in, initial_quality, final_sell_in, final_quality",
        [
            pytest.param("foo", 12, 4, 11, 3, id="basic"),
            pytest.param("foo", 0, 0, -1, 0, id="expired min quality"),
            pytest.param("foo", 0, 1, -1, 0, id="decrease quality"),
            pytest.param("foo", 0, -1, -1, -1, id="quality lt 0"),
        ]
    )
    def test_foo(self, name, initial_sell_in, initial_quality, final_sell_in, final_quality):
        do_update_one(name, initial_sell_in, initial_quality, final_sell_in, final_quality)


class TestGildedRoseAgedBrie:
    def test_aged_brie(self):
        do_update_one(
            name="Aged Brie",
            initial_sell_in=0,
            initial_quality=0,
            final_sell_in=-1,
            final_quality=2
        )


class TestGildedRoseBackStagePasses:
    def test_backstage_passes(self):
        do_update_one(
            name="Backstage passes to a TAFKAL80ETC concert",
            initial_sell_in=0,
            initial_quality=1,
            final_sell_in=-1,
            final_quality=0
        )
