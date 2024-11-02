from functools import reduce


class Problem_list:

    def __init__(self, problems_id: list[str]) -> object:
        self.__problems = problems_id

    def __str__(self) -> str:
        return reduce(
            lambda problem, rest: f"Problema {problem[0] + 1}: {problem[1]} \n"
            + f"Problema {rest[0] + 1}: {rest[1]} \n",
            enumerate(self.__problems),
        )

    async def new_problems() -> None:
        # petición loca a tablon
        pass
