# 4.7 match 문 예제 (Python 3.10+)


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong"


print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))

print()


# | 로 여러 패턴 결합
def http_error_combined(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something else"


print(http_error_combined(401))
print(http_error_combined(200))
