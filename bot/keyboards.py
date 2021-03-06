from vkwave.bots.utils.keyboards import Keyboard, ButtonColor


class Menu:
    __main = Keyboard()
    __main.add_text_button(
        "Новый стих",
        color=ButtonColor.POSITIVE,
        payload={"command": "tasks.new"}
    )
    __main.add_row()
    __main.add_text_button(
        "Топ участников",
        color=ButtonColor.PRIMARY,
        payload={"command": "users.top"}
    )

    @classmethod
    def main(cls):
        return cls.__main.get_keyboard()

    @classmethod
    def clear(cls):
        return Keyboard.get_empty_keyboard()


class Answers:
    @classmethod
    def generate(cls, task_id, answers):
        result = Keyboard(inline=True)
        for i, answer in enumerate(answers):
            result.add_text_button(
                answer,
                color=ButtonColor.SECONDARY,
                payload={
                    "command": "tasks.answer",
                    "args": {"task_id": task_id, "answer": i}
                },
            )
            if i != len(answers) - 1:
                result.add_row()
        return result.get_keyboard()
