def get_val(collection: dict, key, default='git'):
    """
        :param collection: Исходный словарь
        :param key: Ключ для извлечения значения
        :param default: Значение по умолчанию
        :return: Значение из словаря по переданному ключу, если ключ существует. В ином случае возвращается значение
    default
        """
    return collection[key] if key in collection else default