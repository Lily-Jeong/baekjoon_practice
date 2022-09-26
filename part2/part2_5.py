hour, minute = map(int, input().split())
alarm_minute = minute - 45
if alarm_minute > 0:
    print(hour, alarm_minute)
elif alarm_minute == 0:
    print(hour, alarm_minute)
elif alarm_minute < 0:
    if hour > 0:
        print((hour-1), (60 + alarm_minute))
    elif hour == 0:
        print((24 - 1), (60 + alarm_minute))
    elif hour < 0:
        print((24 + hour), (60 + alarm_minute))