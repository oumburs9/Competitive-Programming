"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, query_id):
        employee_map = {e.id: e for e in employees}

        def calculate_total_importance(employee_id):
            current_employee = employee_map[employee_id]
            total_importance = current_employee.importance
            for subordinate_id in current_employee.subordinates:
                total_importance += calculate_total_importance(subordinate_id)
            return total_importance

        return calculate_total_importance(query_id)
