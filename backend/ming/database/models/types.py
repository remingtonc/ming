from sqlalchemy import Column, Integer, func, TypeDecorator, type_coerce, Text


class Password(TypeDecorator):
    impl = Text()

    def bind_expression(self, bindvalue):
        return func.crypt(bindvalue, func.gen_salt("bf", 12))

    class comparator_factory(Text.comparator_factory):
        def __eq__(self, other):
            local_pw = type_coerce(self.expr, Text)
            return local_pw == func.crypt(other, local_pw)
