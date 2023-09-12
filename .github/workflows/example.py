import os
def main():
  print("Hello Python Github Actions!")
  token = os.environ.get("PYTHON_SECRET_TOKEN")
  if not token:
    raise RuntimeError("PYTHON_SECRET_TOKEN is not set!")
  print("Token is set")
if __name__ == '__main__':
  main()
