compiled_code = compile(
    source="""
class _Cat:
    def __init__(self, voice = "Meaow from dynamic class"):
        self.voice = voice
Cat = _Cat
# print(cat.voice)
""",
    filename="<compiled>",
    mode = "exec"
)

exec(compiled_code)

print(Cat().voice)