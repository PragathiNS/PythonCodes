def merge_ranges(data):
    data = sorted(data)
    merged_meetings = [data[0]]

    for curr_meeting_start, curr_meeting_end in data[1:]:
        print (curr_meeting_start, curr_meeting_end)
        last_merged_meet_start, last_merged_meet_end = merged_meetings[-1]

        if (curr_meeting_start <= last_merged_meet_end):
            merged_meetings[-1] = (last_merged_meet_start, max(last_merged_meet_end, curr_meeting_end))
        else:
            merged_meetings.append((curr_meeting_start, curr_meeting_end))
    return merged_meetings

print (merge_ranges([(1, 3), (2, 4)]))
print (merge_ranges([(0,1), (3, 5), (4, 8), (10, 12), (9, 10)]))
