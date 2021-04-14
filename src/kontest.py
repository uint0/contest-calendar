"""
A client for kontests.net
"""

import typing
import requests
import dataclasses
import datetime as dt
import providers

BASE_URL = "https://kontests.net"


@dataclasses.dataclass
class ContestEvent:
    name: str
    url:  str
    start_time: dt.datetime
    end_time: dt.datetime
    duration: int


def _make_event_list(events: typing.List[dict]) -> typing.List[ContestEvent]:
    parse_time = lambda time_str: time_str and dt.datetime.fromisoformat(time_str.replace("Z", "+00:00"))

    return [
        ContestEvent(
            name=evt.get("name"),
            url=evt.get("url"),
            start_time=parse_time(evt.get("start_time")),
            end_time=parse_time(evt.get("end_time")),
            duration=int(evt.get("duration", -1))
        )
        for evt in events
    ]


def get_provider_contests(provider: str) -> typing.List[ContestEvent]:
    provider = providers.get_provider(provider)

    resp = requests.get(f"{BASE_URL}/{provider.kontest_url}")
    resp.raise_for_status()

    return _make_event_list(resp.json())


if __name__ == '__main__':
    print("Avaiable Contests: ", ' '.join(providers.list_providers()))
    print(get_provider_contests(input("Contest: ")))
