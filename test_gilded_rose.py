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
        pytest.param(-2, 10, -3, 8, id="negative sell in"),
        pytest.param(-2, -1, -3, -1, id="negative sell in negative quality"),
        pytest.param(4, 50, 3, 49, id="maximum quality"),
        pytest.param(4, 63, 3, 62, id="above maximum quality"),
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
        pytest.param(4, 50, 3, 50, id="maximum quality"),
    ]
)
def test_aged_brie(initial_sell_in, initial_quality, final_sell_in, final_quality):
    do_update_one("Aged Brie", initial_sell_in, initial_quality, final_sell_in, final_quality)


@pytest.mark.parametrize(
    "initial_sell_in, initial_quality, final_sell_in, final_quality",
    [
        pytest.param(11, 4, 10, 5, id="sell in > 10"),
        pytest.param(10, 4, 9, 6, id="sell in = 10"),
        pytest.param(9, 4, 8, 6, id="between 5 and 10"),
        pytest.param(5, 4, 4, 7, id="sell in = 5"),
        pytest.param(4, 4, 3, 7, id="sell in < 5"),
        pytest.param(-2, 4, -3, 0, id="negative sell in"),
        pytest.param(0, 0, -1, 0, id="expired min quality"),
        pytest.param(0, 1, -1, 0, id="decrease quality"),
        pytest.param(0, -1, -1, 0, id="quality lt 0"),
    ]
)
def test_backstage(initial_sell_in, initial_quality, final_sell_in, final_quality):
    do_update_one("Backstage passes to a TAFKAL80ETC concert", initial_sell_in, initial_quality, final_sell_in,
                  final_quality)


@pytest.mark.parametrize(
    "initial_sell_in, initial_quality, final_sell_in, final_quality",
    [
        pytest.param(12, 80, 12, 80, id="basic"),
        pytest.param(0, 80, 0, 80, id="expired min quality"),
        pytest.param(0, 80, 0, 80, id="decrease quality"),
        pytest.param(0, 80, 0, 80, id="quality lt 0"),
        pytest.param(-2, 80, -2, 80, id="negative sell in"),
    ]
)
def test_sulfuras(initial_sell_in, initial_quality, final_sell_in, final_quality):
    do_update_one("Sulfuras, Hand of Ragnaros", initial_sell_in, initial_quality, final_sell_in, final_quality)
