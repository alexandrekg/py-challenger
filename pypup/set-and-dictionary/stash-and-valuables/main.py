def stash_valuables(stash, valuables):
    count = 0
    for s in stash:
        if s in valuables:
            count += 1

    return count


print(stash_valuables(["rock", "paper", "phone", "phone", "tablet"], ["phone", "tablet"]))
