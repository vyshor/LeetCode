class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        m = len(queries)
        summ = 0
        cols = set()
        rows = set()

        for i in range(m-1, -1, -1):
            (t, idx, v) = queries[i]
            if t == 0:
                if idx in rows:
                    continue

                summ += (n-len(cols))*v
                rows.add(idx)
            else:
                if idx in cols:
                    continue

                summ += (n-len(rows))*v
                cols.add(idx)
            # print("Summ", summ)
        return summ

# class Solution:
#     def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
#         summ = 0
#         cols = {}
#         col_update = {}
#         rows = {}
#         row_update = {}
#
#         for j, (t, i, v) in enumerate(queries):
#             if t == 0:
#                 if i in row_update:
#                     last_update, last_val = row_update[i]
#                 else:
#                     last_update, last_val = -1, 0
#
#                 count = 0
#                 for (k, val) in cols.values():
#                     if k > last_update:
#                         summ -= val
#                         count += 1
#                 summ += n * v - last_val * (n - count)
#
#                 rows[i] = (j, v)
#                 row_update[i] = (j, v)
#             else:
#                 if i in col_update:
#                     last_update, last_val = col_update[i]
#                 else:
#                     last_update, last_val = -1, 0
#
#                 count = 0
#                 for (k, val) in rows.values():
#                     if k > last_update:
#                         summ -= val
#                         count += 1
#                 summ += n * v - last_val * (n - count)
#
#                 cols[i] = (j, v)
#                 col_update[i] = (j, v)
#         return summ
