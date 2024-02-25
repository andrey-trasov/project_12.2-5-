def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    :param collection: элемент словаря
    :param key: ключ словаря
    :param default: значение efault
    :return: возвращает значение из словаря по переданному ключу, или значение efault
    """
    if key in collection:
        return collection[key]
    return default