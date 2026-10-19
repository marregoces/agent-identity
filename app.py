"""A tiny service the github-agent proposes changes to. It does nothing useful on purpose."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("agent identity"))
