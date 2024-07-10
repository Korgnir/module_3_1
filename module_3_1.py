count = 0
def count_calls():
    global count
    count += 1
def string_info(string):
    count_calls()
    return (len(string), str.upper(string), str.lower(string))
def is_contains(a, b):
    count_calls()
    if str(a).lower() in str(b).lower():
        return True
    else:
        return False
print(string_info('Buffalo'))
print(string_info('Moth'))
print(string_info('Nightmare'))
print(is_contains('foggot', ['ArReStant', 'PrisoNER', 'foGGot']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(count)