class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for operation in operations:

            if operation.startswith("-") or operation.endswith("-"):
                result -= 1
            
            elif operation.startswith("+") or operation.endswith("+"):
                result += 1

        return result
