"""Tests for Practice Problem 2: Event Queue Processing"""
import pytest
from practice_problem_2_starter import *


def test_create_event():
    event = create_event("jump", {"power": 10})
    assert event['type'] == "jump"
    assert event['data']['power'] == 10


def test_add_event():
    queue = []
    event = create_event("test")
    add_event(queue, event)
    assert len(queue) == 1


def test_get_next_event():
    queue = [create_event("a"), create_event("b")]
    event = get_next_event(queue)
    assert event['type'] == "a"
    assert len(queue) == 1


def test_filter_events():
    queue = [create_event("jump"), create_event("run"), create_event("jump")]
    jumps = filter_events(queue, "jump")
    assert len(jumps) == 2


def test_clear_events():
    queue = [create_event("a"), create_event("b")]
    clear_events(queue)
    assert len(queue) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
