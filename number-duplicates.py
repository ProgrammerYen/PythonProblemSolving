def duplicate_count(text):
    text = text.lower()
    dup_count = 0
    counted = []
    for i in text:
        if text.count(i) > 1 and i not in counted:
            dup_count += 1
            counted.append(i)
            
    return dup_count
            