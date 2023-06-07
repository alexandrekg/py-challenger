def bonjwa_count(players):
    bonjwas = ['boxer', 'nada', 'iloveoov', 'savior', 'flash']
    return len([p for p in players if p.lower() in bonjwas])


print(bonjwa_count(["Flash", "Jaedong", "Artosis", "Scan"]))
