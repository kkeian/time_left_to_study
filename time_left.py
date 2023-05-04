#!/usr/bin/env python3
from datetime import datetime, timedelta, time
import sys


EXAM_MINUTES = 150


def secToMin(sec: int) -> int:
    return int(sec % pow(60, 2) / 60)


def secToHr(sec: int) -> int:
    return int(sec / (pow(60, 2)))


def main() -> int:
    examDuration = timedelta(minutes=EXAM_MINUTES)
    # Calculate Time of Exam Start
    now = datetime.now()
    nextEngagement = datetime.now().replace(hour=23,minute=58)
    examStartTime = nextEngagement - examDuration

    # Calculate Study Time Remaining
    studyTimeLeft = examStartTime - now
    studyHrsLeft = secToHr(studyTimeLeft.seconds)
    studyMinLeft = secToMin(studyTimeLeft.seconds)
    studyTimeLeft = time(hour=studyHrsLeft,minute=studyMinLeft)


    examStartTimeF = examStartTime.strftime("%H:%M")
    #nextEngagementF = nextEngagement.strftime("%H:%M")
    timeLeftF = studyTimeLeft.strftime("%Hhrs %Mmins")

    #print(f'Prayer at: {nextEngagementF}')
    print(f'Start Exam at: {examStartTimeF}')
    print(f'Time left to study: {timeLeftF}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
