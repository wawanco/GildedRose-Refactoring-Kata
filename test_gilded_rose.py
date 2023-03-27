# -*- coding: utf-8 -*-
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


@pytest.mark.parametrize(
    "initial_sell_in, initial_quality, final_sell_in, final_quality",
    [
        pytest.param(12, 4, 11, 3, id="basic"),
        pytest.param(0, 0, -1, 0, id="expired min quality"),
        pytest.param(0, 1, -1, 0, id="decrease quality"),
        pytest.param(0, -1, -1, -1, id="quality lt 0"),
        pytest.param(-2, -1, -3, -1, id="negative sell in"),
    ]
)
def test_foo(initial_sell_in, initial_quality, final_sell_in, final_quality):
    do_update_one("foo", initial_sell_in, initial_quality, final_sell_in, final_quality)


@pytest.mark.parametrize(
    "initial_sell_in, initial_quality, final_sell_in, final_quality",
    [
        pytest.param(12, 4, 11, 5, id="basic"),
        pytest.param(0, 0, -1, 2, id="expired min quality"),
        pytest.param(0, 1, -1, 3, id="decrease quality"),
        pytest.param(0, -1, -1, 1, id="quality lt 0"),
        pytest.param(-2, -1, -3, 1, id="negative sell in"),
    ]
)
def test_aged_brie(initial_sell_in, initial_quality, final_sell_in, final_quality):
    do_update_one("Aged Brie", initial_sell_in, initial_quality, final_sell_in, final_quality)


@pytest.mark.parametrize(
    "initial_sell_in, initial_quality, final_sell_in, final_quality",
    [
        pytest.param(12, 4, 11, 5, id="basic"),
        pytest.param(0, 0, -1, 0, id="expired min quality"),
        pytest.param(0, 1, -1, 0, id="decrease quality"),
        pytest.param(0, -1, -1, 0, id="quality lt 0"),
        pytest.param(-2, -1, -3, 0, id="negative sell in"),
    ]
)
def test_backstage(initial_sell_in, initial_quality, final_sell_in, final_quality):
    do_update_one("Backstage passes to a TAFKAL80ETC concert", initial_sell_in, initial_quality, final_sell_in, final_quality)
