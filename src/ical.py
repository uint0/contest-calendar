import ics
import kontest


def make_ical(provider: str):
    cal = ics.Calendar()
    contest_data = kontest.get_provider_contests(provider)
    
    for contest in contest_data:
        cal.events.add(ics.Event(
            name=contest.name,
            begin=contest.start_time,
            end=contest.end_time,
            url=contest.url
        ))
    
    return cal


if __name__ == '__main__':
    ical = make_ical(input("Contest: "))
    print(ical)
