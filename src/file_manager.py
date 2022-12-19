import os

class FileManager:
  def __init__(self, path: str):
    self.__path = path

    if not os.path.isdir(self.__path):
      os.mkdir(self.__path)

  def create(self, filename: str, content: str = "") -> None:
    full_path = self.__full_path(filename)
    if os.path.exists(full_path):
      raise FileExistsError(full_path)

    with open(full_path, "w") as file:
      file.write(content)
      file.close()

  def list(self) -> list[str]:
    return os.listdir(self.__path)

  def read(self, filename: str) -> str:
    f = open(self.__full_path(filename), "r")
    sql = f.read()
    f.close()
    return sql

  def __full_path(self, filename: str) -> str:
    return f"{self.__path}/{filename}"
