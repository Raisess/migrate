class AbstractCommand:
  @staticmethod
  def SliceArguments(argv: list[str]) -> list[str]:
    return argv[2:]

  def __init__(self, command: str, required_args_len: int = 0):
    self.__command = command
    self.__required_args_len = required_args_len

  def get_command(self) -> str:
    return self.__command

  def get_required_args_len(self) -> int:
    return self.__required_args_len

  def validate_args_len(self, args: list[str], exception: Exception) -> None:
    if len(args) < self.get_required_args_len():
      raise exception

  def handle(self, args: list[str]) -> None:
    pass
