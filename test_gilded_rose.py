# -*- coding: utf-8 -*-
import unittest
from typing import List

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
    def test_foo(self):
        do_update_one(
            name="foo",
            initial_sell_in=0,
            initial_quality=0,
            final_sell_in=-1,
            final_quality=0
        )

    def test_positive_quality(self):
        do_update_one(
            name="foo",
            initial_sell_in=0,
            initial_quality=1,
            final_sell_in=-1,
            final_quality=0
        )


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
