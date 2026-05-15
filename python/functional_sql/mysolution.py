from functools import cmp_to_key
from itertools import product
from preloaded import (
    DuplicateFromError,
    DuplicateSelectError,
    DuplicateGroupByError,
    DuplicateOrderByError,
)


class Query:
    def __init__(self):
        self._select = False
        self._from = False
        self._group_by = False
        self._order_by = False

        self.select_fn = None
        self.tables = ()
        self.where_clauses = []
        self.group_funcs = ()
        self.having_clauses = []
        self.order_fn = None

    def select(self, fn=None):
        if self._select:
            raise DuplicateSelectError()

        self._select = True
        self.select_fn = fn
        return self

    def from_(self, *tables):
        if self._from:
            raise DuplicateFromError()

        self._from = True
        self.tables = tables
        return self

    def where(self, *predicates):
        self.where_clauses.append(predicates)
        return self

    def group_by(self, *funcs):
        if self._group_by:
            raise DuplicateGroupByError()

        self._group_by = True
        self.group_funcs = funcs
        return self

    def having(self, *predicates):
        self.having_clauses.append(predicates)
        return self

    def order_by(self, fn):
        if self._order_by:
            raise DuplicateOrderByError()

        self._order_by = True
        self.order_fn = fn
        return self

    def execute(self):
        data = self._exec_from()
        data = self._apply_filters(data, self.where_clauses)

        if self.group_funcs:
            data = self._group(data, self.group_funcs)

        data = self._apply_filters(data, self.having_clauses)

        if self._select:
            if self.select_fn is not None:
                data = [self.select_fn(x) for x in data]

        if self.order_fn:
            data = sorted(data, key=cmp_to_key(self.order_fn))

        return data

    def _exec_from(self):
        if not self.tables:
            return []

        if len(self.tables) == 1:
            return list(self.tables[0])

        return [list(x) for x in product(*self.tables)]

    def _apply_filters(self, data, clauses):
        for predicates in clauses:
            data = [
                x for x in data
                if any(predicate(x) for predicate in predicates)
            ]
        return data

    def _group(self, data, funcs):
        fn = funcs[0]
        grouped = {}

        for item in data:
            key = fn(item)
            grouped.setdefault(key, []).append(item)

        result = []

        for key, values in grouped.items():
            if len(funcs) > 1:
                values = self._group(values, funcs[1:])

            result.append([key, values])

        return result


def query():
    return Query()

# original kata: https://www.codewars.com/kata/545434090294935e7d0010ab
# my solution: https://www.codewars.com/kata/reviews/67bb2fce152163bfd15afc73/groups/6a06c6cbb4bf51cedf1574f9
