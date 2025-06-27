import random
import pytest

PLATFORM = "Linux"

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_rerun():
    assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_run_1(self):
        assert random.choice([True, False])

    def test_run_2(self):
        assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM=="Linux")
def test_rerun_with_condition(platform):
    assert random.choice([True, False])