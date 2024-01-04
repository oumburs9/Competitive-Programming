class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        
        taskIndex = 0  
        answer = 0

        for processingTime in processorTime:
            currentMax = 0
            taskCount = 0

            # process up to 4 tasks for the current processor
            while taskIndex < len(tasks) and taskCount < 4:
                currentMax = max(currentMax, processingTime + tasks[taskIndex])
                taskIndex += 1
                taskCount += 1

            answer = max(answer, currentMax)

        return answer


        