class Result:
    pass

instance = Result()
class_name = type(instance).__name__
print(f"The class name of the instance is: {class_name}")
